import requests, json

url = 'https://httpbin.org/put'
payload = {'nombre':'Maximiliano', 'curso':'python', 'nivel':'B1' }

response = requests.put(url, data=json.dumps(payload)) 

if response.status_code == 200:
    headers_response = response.headers #Dic
    server_response = headers_response['Server']
    print(server_response)