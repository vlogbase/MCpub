import requests

url = 'https://liveinfo.org/api/rewrite_links'  # Use the actual URL
headers = {'Content-Type': 'application/json'}
data = {
    'urls': ['https://example.com'],  # Note: 'urls' should be a list
    'SkimpubID': '44501'  # Replace with a valid Skimlinks Publisher ID
}

response = requests.post(url, json=data, headers=headers)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
