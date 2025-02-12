import json
import requests
import os

def lambda_handler(event, context):
    api_url = os.environ['API_URL']
    headers = {"X-Siemens-Auth": "test"}
    payload = {
        "subnet_id": event["subnet_id"],
        "full_name": event["full_name"],
        "email": event["email"]
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return {
        "statusCode": response.status_code,
        "body": response.json()
    }
}
