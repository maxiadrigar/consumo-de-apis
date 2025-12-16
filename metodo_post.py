import requests, json

url = 'https://httpbin.org/post'
payload = {'nombre':'Maximiliano', 'curso':'python', 'nivel':'B1' }

response = requests.post(url, data=json.dumps(payload)) #Internamente json toma este diccionario y lo va a deserializar

if response.status_code == 200:
     print(response.json())
    

# Deserializar sigfigica tomar el diccionario y convertirlo a json