import requests

url = 'https://monetizechatbots.replit.app/api/rewrite_links'  # Replace with your actual Replit URL
headers = {'Content-Type': 'application/json'}
data = {'url': 'https://example.com'}

response = requests.post(url, json=data, headers=headers)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
