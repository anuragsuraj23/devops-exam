import json
import requests

def lambda_handler(event, context):
    api_url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    headers = {"X-Siemens-Auth": "test"}
    
    payload = {
        "subnet_id": event.get("subnet_id"),
        "full_name": "Anurag Dangi",
        "email": "anurag.suraj@gmail.com"
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    return {
        "statusCode": response.status_code,
        "body": response.json()
    }
