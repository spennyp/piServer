import requests

url = "http://192.168.0.200:8060/tell-slack" 

data = {"channel": "octoprint", "text": "A print just started!"}
requests.post(url, json=data)
