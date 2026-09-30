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

    # Vocabulary Richness
    unique_words = len(set(words))
    ttr = unique_words / num_words if num_words > 0 else 0
    
    # Shannon Entropy (Predictability)
    from collections import Counter
    import math
    word_counts = Counter(words)
    entropy = sum(-(count/num_words) * math.log2(count/num_words) for count in word_counts.values()) if num_words > 0 else 0

    return [
        avg_word_length,
        avg_line_length,
        max_line_length,
        blank_ratio,
        comment_ratio,
        avg_indent,
        ttr,
        entropy
    ]

# --- 2. LOAD DATASET ---
dataset_path = os.path.join(os.path.dirname(__file__), "dataset.json")

training_data = []
labels = []

if os.path.exists(dataset_path):
    print(f"📦 Loading real dataset from {dataset_path}...")
    with open(dataset_path, "r") as f:
        data = json.load(f)
        for item in data:
            training_data.append(extract_features(item["code"]))
            labels.append(item["label"])
else:
    print("⚠️ WARNING: dataset.json not found! Falling back to dummy data.")
    print("Please run `python3 dataset_builder.py` to generate real data.")
    # 0 = Human, 1 = AI
    human_1 = "def f(x):\n  # add one\n  y = x+1\n  return y\n\n\n"
    human_2 = "let i=0;\nfor(;i<10;i++){\n console.log(i);\n}"
    ai_1 = "# Function to calculate sum\ndef calculate_sum(val_one, val_two):\n    # Return result\n    return val_one + val_two"
    ai_2 = "// Loop counter\nfor (let loopIndex = 0; loopIndex < 10; loopIndex++) {\n    console.log(loopIndex);\n}"

    training_data = [
        extract_features(human_1), extract_features(human_2),
        extract_features(ai_1), extract_features(ai_2)
    ]
    labels = [0, 0, 1, 1]

# --- 3. TRAIN THE RANDOM FOREST ---
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42) # Increased to 100 trees for better accuracy
rf_model.fit(training_data, labels)
print(f"🌲 Random Forest trained on {len(training_data)} examples!")

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
