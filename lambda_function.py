import json
import requests

def lambda_handler(event, context):
    url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    
    payload = {
        "subnet_id": event["subnet_id"],
        "full_name": event["full_name"],
        "email": event["email"]
    }
    
    headers = {"X-Siemens-Auth": "test"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    return {
        "statusCode": response.status_code,
        "body": response.text
    }
