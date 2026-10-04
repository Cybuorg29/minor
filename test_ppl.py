import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import math

device = "cpu"
model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id).to(device)

def get_perplexity(text):
    inputs = tokenizer(text, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss = outputs.loss
    return math.exp(loss.item())

ai_code = """import pytest
def classify_ai_score(score: float) -> str:
    if not (0.0 <= score <= 1.0):
        raise ValueError("Score must be between 0.0 and 1.0")
    if score >= 0.8: return "High Likelihood AI"
    return "Likely Human"
"""

human_code = """
var1 = 0
for xyz in range(10):
    print("hello " + str(xyz))
    var1 += xyz
print(var1)
"""

print(f"AI Perplexity: {get_perplexity(ai_code):.2f}")
print(f"Human Perplexity: {get_perplexity(human_code):.2f}")
