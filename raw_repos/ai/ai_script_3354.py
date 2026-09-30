"""
Write a code to fetch the last 4 commits of a git repository
"""

import requests

user = 'rnyagah'
repo = 'GPT-Evaluation'

url = f'https://api.github.com/repos/{user}/{repo}/commits'

response = requests.get(url)
data = response.json()

# get the last 4 commits
commits = data[:4]

for commit in commits:
    print(f'commit {commit["sha"]}: {commit["commit"]["message"]}')