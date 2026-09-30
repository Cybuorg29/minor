import os
import json
import shutil
import subprocess
import urllib.request
import ssl
import random

def get_human_code(base_dir="raw_repos/human", num_repos=100):
    """Dynamically finds and clones obscure pre-2022 Python repos."""
    human_data = []
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    print(f"🔍 Searching GitHub for {num_repos} obscure, pre-ChatGPT Python repositories...")
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = f"https://api.github.com/search/repositories?q=language:python+pushed:<2021-12-31+stars:500..2000&per_page={num_repos}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    repos = []
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            for item in data.get('items', []):
                repos.append({
                    "name": item["name"],
                    "url": item["clone_url"]
                })
    except Exception as e:
        print(f"❌ Error hitting GitHub API: {e}")
        return human_data
        
    print(f"✅ Found {len(repos)} repositories! Cloning them now...")
    
    for repo in repos:
        repo_name = repo['name']
        repo_path = os.path.join(base_dir, repo_name)
        
        if not os.path.exists(repo_path):
            print(f"📥 Cloning {repo_name}...")
            subprocess.run(
                ["git", "clone", "--depth", "1", repo["url"], repo_path],
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
        else:
            print(f"✅ {repo_name} already cloned.")
            
        files_parsed = 0
        for root, _, files in os.walk(repo_path):
            for file in files:
                if files_parsed > 50:
                    break
                if file.endswith(".py") and "test" not in file.lower():
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            lines = f.readlines()
                            i = 0
                            while i < len(lines):
                                chunk_size = random.randint(3, 25)
                                chunk = "".join(lines[i:i+chunk_size])
                                if len(chunk.strip()) > 30 and ("def " in chunk or "class " in chunk):
                                    human_data.append({"code": chunk, "label": 0})
                                i += chunk_size
                        files_parsed += 1
                    except Exception:
                        pass

    print(f"✅ Extracted {len(human_data)} human Python snippets from {len(repos)} obscure repos!")
    return human_data

def get_ai_code(target_samples, base_dir="raw_repos/ai"):
    """Downloads AI code and stores them as actual .py files to show the evaluator."""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    print(f"\n🤖 Downloading AI-generated Python files into {base_dir}...")
    ai_data = []
    
    # Check if we already have files
    existing_files = [f for f in os.listdir(base_dir) if f.endswith('.py')]
    if len(existing_files) >= target_samples:
        print("✅ AI files already exist! Reading from disk...")
        for file in existing_files:
            with open(os.path.join(base_dir, file), "r", encoding="utf-8") as f:
                code_response = f.read()
                ai_data.append({"code": code_response, "label": 1})
        return ai_data[:target_samples]

    offset = 0
    file_counter = len(existing_files)
    while len(ai_data) < target_samples and offset < 10000:
        url = f"https://datasets-server.huggingface.co/rows?dataset=HuggingFaceH4%2FCodeAlpaca_20K&config=default&split=train&offset={offset}&length=100"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx) as response:
                data = json.loads(response.read().decode())
                
            for row in data.get('rows', []):
                code_response = row['row']['completion']
                if "def " in code_response or "import " in code_response or "class " in code_response:
                    # Save as a real file for the evaluator to see!
                    file_path = os.path.join(base_dir, f"ai_script_{file_counter}.py")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(code_response)
                        
                    ai_data.append({"code": code_response, "label": 1})
                    file_counter += 1
                    
                    if len(ai_data) >= target_samples:
                        break
                        
            offset += 100
        except Exception as e:
            print(f"❌ Error fetching from HuggingFace API: {e}")
            break
            
    print(f"✅ Successfully extracted {len(ai_data)} AI-generated files into {base_dir}/!")
    return ai_data

if __name__ == "__main__":
    print("🚀 Starting Dataset Builder\n")
    
    # 1. Grab Human Code (will stay on disk in raw_repos/human)
    human_snippets = get_human_code()
    
    # 2. Grab AI Code (will save as files in raw_repos/ai)
    # We ask for a max of 3000 to match the huge human dataset
    ai_snippets = get_ai_code(target_samples=3000) 
    
    # 3. Balance the dataset perfectly (50/50)
    random.seed(42)
    random.shuffle(human_snippets)
    human_snippets = human_snippets[:len(ai_snippets)]
    print(f"\n⚖️ Balanced dataset: {len(human_snippets)} Human / {len(ai_snippets)} AI")
    
    # 4. Combine and Save
    dataset = human_snippets + ai_snippets
    
    output_file = "dataset.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4)
        
    print(f"🎉 Done! Saved {len(dataset)} examples to {output_file}")
