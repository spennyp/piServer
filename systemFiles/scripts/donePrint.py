import requests

url = "http://192.168.0.200:8060/tell-slack" 

data = {"channel": "octoprint", "text": "A print just ended!"}
requests.post(url, json=data)
