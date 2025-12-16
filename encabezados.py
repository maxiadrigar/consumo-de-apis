import requests, json

url = 'https://httpbin.org/post'
payload = {'nombre':'Maximiliano', 'curso':'python', 'nivel':'B1' }
headers = {'Content-Type': 'application/json', 'access-token': '12345'}
#De esta forma le digo al servidor que estoy enviando datos en formato json

response = requests.post(url, data=json.dumps(payload), headers=headers) 

if response.status_code == 200:
    #Leer encabezados
    headers_response = response.headers #Dic
    server_response = headers_response['Server']
    print(server_response)