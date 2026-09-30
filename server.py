from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detector import extract_features, rf_model

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
    
    # 2. Ask the Random Forest to predict
    prediction_num = rf_model.predict([features])[0]
    
    # 3. Calculate confidence %
    confidence = rf_model.predict_proba([features])[0][prediction_num] * 100
    
    result_label = "AI" if prediction_num == 1 else "Human"

    # 4. Generate Explainability Reason
    reasons = []
    if result_label == "AI":
        if features[3] < 0.2:
            reasons.append("It is unnaturally dense with very few blank lines.")
        if features[5] < 4.5:
            reasons.append("It uses strict, textbook-perfect indentation patterns.")
        if features[0] < 5.5:
            reasons.append("The variable names are highly generic and short.")
        if features[6] < 0.5:
            reasons.append("The vocabulary is extremely repetitive (low Type-Token Ratio).")
        if features[7] < 4.0:
            reasons.append("The code has low entropy, making it highly predictable.")
        if not reasons:
            reasons.append("The overall code structure strongly aligns with LLM generation patterns.")
    else:
        if features[3] >= 0.2:
            reasons.append("It has a natural, organic spacing of blank lines typical of humans.")
        if features[5] >= 4.5:
            reasons.append("It uses deeper, more variable nesting and indentation.")
        if features[0] >= 5.5:
            reasons.append("It uses complex, context-specific variable names.")
        if features[6] >= 0.5:
            reasons.append("It uses a rich, varied vocabulary (high Type-Token Ratio).")
        if features[7] >= 4.0:
            reasons.append("The code has high entropy, indicating unpredictable human phrasing.")
        if not reasons:
            reasons.append("The structural variability is very messy and human-like.")

    return {
        "prediction": result_label,
        "confidence": round(confidence, 1),
        "reason": " ".join(reasons)
    }

@app.get("/")
async def root():
    return {"message": "AI Code Detector Server is running!"}
