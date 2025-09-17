import requests
import json
import re

with open('content.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Prepare the API request
url = "https://api.github.com/markdown"
headers = {
    "Accept": "text/html",
    "X-GitHub-Api-Version": "2022-11-28"
}
data = {
    "text": markdown_content
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    pattern = r'(<section>).*?(</section>)'
    replacement = r'\1' + response.text + r'\2'
    updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print("Conversion successful!")
else:
    print(f"Error: {response.status_code} - {response.text}")
