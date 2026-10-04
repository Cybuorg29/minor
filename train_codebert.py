import json
import torch
import joblib
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

print("🤖 Loading CodeBERT...")
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')
model = AutoModel.from_pretrained('microsoft/codebert-base')
model.eval()

def get_codebert_embedding(code):
    inputs = tokenizer(code, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Robust Mean Pooling instead of fragile [CLS] token
    hidden = outputs.last_hidden_state
    mask = inputs['attention_mask'].unsqueeze(-1)
    emb = (hidden * mask).sum(1) / mask.sum(1)
    return emb[0].numpy()

import os
import random

def load_from_raw_repos(samples_per_class=500):
    dataset = []
    
    # 1. Load AI Data directly from files
    print("📂 Scanning raw_repos/ai...")
    ai_dir = "raw_repos/ai"
    if os.path.exists(ai_dir):
        ai_files = [os.path.join(ai_dir, f) for f in os.listdir(ai_dir) if f.endswith('.py')]
        random.shuffle(ai_files)
        for f in ai_files[:samples_per_class]:
            try:
                with open(f, "r", encoding="utf-8") as file:
                    dataset.append({"code": file.read(), "label": 1})
            except Exception:
                pass

    # 2. Load Human Data directly from GitHub repos
    print("📂 Scanning raw_repos/human...")
    human_dir = "raw_repos/human"
    human_snippets = []
    if os.path.exists(human_dir):
        for root, _, files in os.walk(human_dir):
            for file in files:
                if file.endswith('.py') and 'test' not in file.lower():
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            lines = f.readlines()
                            if len(lines) > 5:
                                # Just grab the first viable chunk to keep scanning fast
                                chunk_size = random.randint(3, 25)
                                chunk = "".join(lines[:chunk_size])
                                if len(chunk.strip()) > 30 and ("def " in chunk or "class " in chunk):
                                    human_snippets.append(chunk)
                    except Exception:
                        pass
                        
    random.shuffle(human_snippets)
    for snippet in human_snippets[:samples_per_class]:
        dataset.append({"code": snippet, "label": 0})
        
    random.shuffle(dataset)
    return dataset

if __name__ == "__main__":
    subset = load_from_raw_repos(samples_per_class=500)

    print(f"🧠 Extracting 768-D Semantic Embeddings for {len(subset)} examples...")
    X = []
    y = []
    
    start = time.time()
    for i, item in enumerate(subset):
        if i % 100 == 0 and i > 0:
            print(f"  ...processed {i}/{len(subset)} in {time.time() - start:.1f}s")
        
        try:
            emb = get_codebert_embedding(item['code'])
            X.append(emb)
            y.append(item['label'])
        except Exception:
            pass

    print("🌲 Training CodeBERT Classifier...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ CodeBERT Classifier Accuracy: {acc*100:.1f}%")
    
    joblib.dump(clf, "codebert_model.pkl")
    print("💾 Saved model to codebert_model.pkl")
