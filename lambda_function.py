import json
import os
import requests

def lambda_handler(event, context):
    api_url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    headers = {"X-Siemens-Auth": "test"}

    payload = {
        "subnet_id": os.environ['SUBNET_ID'],
        "full_name": os.environ['FULL_NAME'],
        "email": os.environ['EMAIL']
    }

    response = requests.post(api_url, json=payload, headers=headers)
    
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
