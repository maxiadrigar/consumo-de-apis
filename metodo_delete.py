import requests, json

url = 'https://httpbin.org/delete'
payload = {'nombre':'Maximiliano', 'curso':'python', 'nivel':'B1' }

response = requests.delete(url, data=json.dumps(payload)) 

if response.status_code == 200:
    headers_response = response.headers #Dic
    server_response = headers_response['Server']
    print(server_response)