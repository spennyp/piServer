import logging
import traceback
import os
import requests

errorWebhook = os.environ["ERROR_WEBHOOK"]

def handleError(e):
    try:
        stackTrace = traceback.print_exc()
        logging.error(f"Error: {e} \n\nTraceback: {stackTrace}")
        data = {"text": f"Error: {e} \n\nTraceback: {stackTrace}"}
        response = requests.post(errorWebhook, json=data)
        response.raise_for_status()
    except Exception as e:
        stackTrace = traceback.print_exc() 
        logging.critical(f"ERROR WHILE HANDLING ERROR: {e} \n\nTraceback: {stackTrace}")
