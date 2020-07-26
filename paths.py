from flask_restful import Resource, Api, request
from errorHandler import handleError
import requests
from config import secrets


# Extracting secrets
octoprintWebhook = secrets["OCTOPRINT_WEBHOOK"]

class TellSlack(Resource):
    def get(self):
        return "This path does not have a get request", 400
    def put(self):
        return "This path does not have a put request", 400 
    def post(self):
        try:
            data = request.json
            channel = data["channel"]
            if(channel == "octoprint"):
                payload = {"text": data["text"]}
                response = requests.post(octoprintWebhook, json=payload)
                response.raise_for_status()
            else:
                raise Exception(f"No webhook exists for the channel name {channel}")
            return "success", 200
        except Exception as e:
            handleError(e)
            return f"Error: {e}", 400
