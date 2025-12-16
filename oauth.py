import requests

client_id = 'Ov23libwKA9uQN1YublP'
client_secret = 'ab11bc1ca0a6ff875fb0a29d3ba1c2d36c1e540e'
code = '5d2f30157225f7b4dddf'

url = 'https://github.com/login/oauth/access_token'

payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
headers = {'Accept': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    response_json = response.json()
    print(response_json)

