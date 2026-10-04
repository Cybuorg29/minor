from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detector import extract_features, rf_model
import joblib
import torch
from transformers import AutoTokenizer, AutoModel

# Load CodeBERT if available
try:
    codebert_rf = joblib.load("codebert_model.pkl")
    cb_tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')
    cb_model = AutoModel.from_pretrained('microsoft/codebert-base')
    cb_model.eval()
    CODEBERT_LOADED = True
    print("✅ CodeBERT Backend Loaded!")
except Exception as e:
    CODEBERT_LOADED = False
    print("⚠️ CodeBERT model not loaded:", e)

app = FastAPI(title="AI Code Detector API")

# Allow frontend to communicate with API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeSubmission(BaseModel):
    code: str

@app.post("/detect")
async def detect_ai_code(submission: CodeSubmission):
    # 1. Turn the code into numbers (features)
    # [avg_word_length, avg_line_length, max_line_length, blank_ratio, comment_ratio, avg_indent]
    features = extract_features(submission.code)
    
    # 2. Ask the TF-IDF Model to predict based on raw text vocabulary
    probs = rf_model.predict_proba([submission.code])[0]
    prob_human = probs[0]
    prob_ai = probs[1]
    
    if prob_ai >= 0.20:
        result_label = "AI"
        confidence = prob_ai * 100
    elif prob_human >= 0.85:
        result_label = "Human"
        confidence = prob_human * 100
    else:
        result_label = "Uncertain"
        confidence = max(prob_ai, prob_human) * 100

    # 4. Generate Explainability Reason
    reasons = []
    if result_label == "AI":
        if features[3] < 0.2:
            reasons.append("It is unnaturally dense with very few blank lines.")
        if features[5] < 4.5:
            reasons.append("It uses strict, textbook-perfect indentation patterns.")
        if features[0] < 5.5:
            reasons.append("The variable names are highly generic and short.")
        if not reasons:
            reasons.append("The overall code structure strongly aligns with LLM generation patterns.")
    elif result_label == "Human":
        if features[3] >= 0.2:
            reasons.append("It has a natural, organic spacing of blank lines typical of humans.")
        if features[5] >= 4.5:
            reasons.append("It uses deeper, more variable nesting and indentation.")
        if features[0] >= 5.5:
            reasons.append("It uses complex, context-specific variable names.")
        if not reasons:
            reasons.append("The structural variability is very messy and human-like.")
    elif result_label == "Uncertain":
        reasons.append("The code contains a mix of human-like phrasing and AI-like structural density.")

    # 5. Line-by-Line Heatmap Analysis (Sliding Window)
    lines = submission.code.split('\n')
    line_scores = []
    
    for i in range(len(lines)):
        # If it's a completely empty line, default to 0 to avoid messy visual noise
        if not lines[i].strip():
            line_scores.append(0.0)
            continue
            
        # Create a 5-line context window around the current line
        start = max(0, i - 2)
        end = min(len(lines), i + 3)
        window_code = '\n'.join(lines[start:end])
        
        w_features = extract_features(window_code)
        prob_ai = rf_model.predict_proba([window_code])[0][1]
        line_scores.append(round(prob_ai, 3))

    return {
        "prediction": result_label,
        "confidence": round(confidence, 1),
        "reason": " ".join(reasons),
        "line_scores": line_scores
    }

@app.get("/")
async def root():
    return {"message": "AI Code Detector Server is running!"}

@app.post("/detect-codebert")
async def detect_ai_codebert(submission: CodeSubmission):
    if not CODEBERT_LOADED:
        return {"error": "CodeBERT model not trained yet."}
        
    code = submission.code
    
    # Extract embedding
    inputs = cb_tokenizer(code, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = cb_model(**inputs)
    
    # Robust Mean Pooling instead of fragile CLS token
    hidden = outputs.last_hidden_state
    mask = inputs['attention_mask'].unsqueeze(-1)
    emb = (hidden * mask).sum(1) / mask.sum(1)
    emb = emb[0].numpy()
    
    # Predict
    prob = codebert_rf.predict_proba([emb])[0]
    
    prob_ai = prob[1]
    prob_human = prob[0]
    
    if prob_ai >= 0.6:
        result_label = "AI"
        confidence = prob_ai * 100
    elif prob_human >= 0.6:
        result_label = "Human"
        confidence = prob_human * 100
    else:
        result_label = "Uncertain"
        confidence = max(prob_ai, prob_human) * 100
    
    reasons = [f"CodeBERT's Deep Learning Transformer is {confidence:.1f}% confident this is {result_label} code based on semantic embeddings."]
    
    return {
        "prediction": result_label,
        "confidence": round(confidence, 1),
        "reason": " ".join(reasons),
        "line_scores": []
    }

import tempfile
import subprocess
import os

class RepoRequest(BaseModel):
    url: str

@app.post("/scan-repo")
async def scan_repo(req: RepoRequest):
    temp_dir = tempfile.mkdtemp()
    subprocess.run(["git", "clone", "--depth", "1", req.url, temp_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    files_data = []
    for root_dir, _, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root_dir, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()
                    if len(code.strip()) < 10:
                        continue
                        
                    # TF-IDF Pipeline expects raw code
                    prob_ai = rf_model.predict_proba([code])[0][1]
                    rel_path = os.path.relpath(path, temp_dir)
                    
                    files_data.append({
                        "filename": rel_path,
                        "code": code,
                        "ai_score": round(prob_ai, 3)
                    })
                except Exception:
                    pass
                    
    files_data.sort(key=lambda x: x["ai_score"], reverse=True)
    return {"files": files_data[:50]} # Return top 50 files to avoid payload overload
