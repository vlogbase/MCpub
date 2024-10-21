import requests

url = 'https://liveinfo.org/api/rewrite_links'  # Use the actual URL
headers = {'Content-Type': 'application/json'}
data = {
    'url': 'https://example.com',
    'cust_id': '44501'  # Replace with a valid customer ID
}

response = requests.post(url, json=data, headers=headers)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
