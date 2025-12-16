import requests, json

url = 'https://httpbin.org/get'
args = {'nombre':'Maximiliano', 'curso':'python', 'nivel':'B1' }

response = requests.get(url, params=args)
    
if response.status_code == 200:
        
    response_json = response.json() # Esta forma me resulta mas facil
    origin = response_json['origin']
    print(origin)
        
    """"
    response_json = json.loads(response.text)
    origin = response_json['origin']
    print(origin)
    """