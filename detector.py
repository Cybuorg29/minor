import re
import os
import json
import math
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# --- 1. EXTRACTOR: Turns code into numbers ---
def extract_features(code: str):
    lines = code.split('\n')
    num_lines = len(lines) if lines else 1
    
    # NLP Features
    words = re.findall(r'\b\w+\b', code.lower())
    num_words = len(words) if words else 1
    avg_word_length = sum(len(w) for w in words) / num_words
    
    # Structure Features (Highly length independent)
    line_lengths = [len(line) for line in lines]
    avg_line_length = sum(line_lengths) / num_lines
    max_line_length = max(line_lengths) if line_lengths else 0
    
    # Empty Lines
    blank_lines = sum(1 for line in lines if not line.strip())
    blank_ratio = blank_lines / num_lines
    
    # Comments
    comments = sum(1 for line in lines if line.strip().startswith('#') or line.strip().startswith('//'))
    comment_ratio = comments / num_lines
    
    # Indentation (AI code often has perfect standard 4-space indents)
    leading_spaces = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    avg_indent = (sum(leading_spaces) / len(leading_spaces)) if leading_spaces else 0

    # AST Features (Logic Complexity)
    import ast
    num_funcs = 0
    num_ifs = 0
    num_loops = 0
    ast_depth = 0
    try:
        tree = ast.parse(code)
        num_funcs = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        num_ifs = sum(1 for node in ast.walk(tree) if isinstance(node, ast.If))
        num_loops = sum(1 for node in ast.walk(tree) if isinstance(node, (ast.For, ast.While)))
        
        def get_depth(node):
            return 1 + max([0] + [get_depth(child) for child in ast.iter_child_nodes(node)])
        ast_depth = get_depth(tree)
    except SyntaxError:
        pass

    return [
        avg_word_length,
        avg_line_length,
        max_line_length,
        blank_ratio,
        comment_ratio,
        avg_indent,
        num_funcs,
        num_ifs,
        num_loops,
        ast_depth
    ]

# --- 2. LOAD DATASET & TRAIN ROBUST TF-IDF MODEL ---
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

dataset_path = os.path.join(os.path.dirname(__file__), "dataset.json")

training_texts = []
labels = []

if os.path.exists(dataset_path):
    print(f"📦 Loading real dataset from {dataset_path}...")
    with open(dataset_path, "r") as f:
        data = json.load(f)
        for item in data:
            training_texts.append(item["code"])
            # Ensure label is 1 for AI, 0 for Human
            lbl = 1 if item["label"] in [1, "AI"] else 0
            labels.append(lbl)

    # 🚀 Inject Synthetic AI PyTest examples to remove the dataset bias!
    synthetic_ai_tests = [
        "import pytest\ndef test_classify():\n    assert classify_score(0.9) == 'AI'",
        "import pytest\ndef test_function_boundaries():\n    with pytest.raises(ValueError):\n        my_func(-1)",
        "import pytest\n@pytest.fixture\ndef setup_data():\n    return [1, 2, 3]\n\ndef test_data(setup_data):\n    assert len(setup_data) == 3",
        "import unittest\nclass TestMyCode(unittest.TestCase):\n    def test_basic(self):\n        self.assertEqual(1, 1)",
        "def test_ai_score_out_of_bounds():\n    with pytest.raises(ValueError):\n        classify_ai_score(-0.1)"
    ]
    for test_code in synthetic_ai_tests:
        training_texts.append(test_code)
        labels.append(1) # Label as AI
        
else:
    print("⚠️ WARNING: dataset.json not found! Falling back to dummy data.")
    training_texts = ["def ai(): pass", "def human(): pass"]
    labels = [1, 0]

print("🚀 Training highly robust TF-IDF Model...")
rf_model = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=2000, stop_words='english')),
    ('clf', LogisticRegression(random_state=42, max_iter=1000, class_weight="balanced"))
])

rf_model.fit(training_texts, labels)
print(f"✅ TF-IDF Model trained on {len(training_texts)} snippets!")

# --- 4. PREDICT NEW CODE (For direct testing) ---
def detect_ai_code(new_code):
    features = extract_features(new_code)
    prediction = rf_model.predict([features])[0]
    confidence = rf_model.predict_proba([features])[0][prediction] * 100
    
    who = "🤖 AI" if prediction == 1 else "🧑‍💻 Human"
    print(f"Prediction: {who} ({confidence:.1f}% sure)")

if __name__ == "__main__":
    print("--- Test 1: Messy Human Code ---")
    detect_ai_code("def do_thing(a,b):\n  tmp = a+b\n  return tmp # done\n\n")
    
    print("\n--- Test 2: Perfect AI Code ---")
    detect_ai_code("# This function calculates the sum\ndef add_two_numbers(first, second):\n    return first + second")
