import json
import urllib3
import os

def lambda_handler(event, context):
    url = os.getenv("API_URL", "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data")
    headers = {
        "Content-Type": "application/json",
        "X-Siemens-Auth": "test"
    }

    payload = {
        "subnet_id": event.get("subnet_id", "unknown"),
        "full_name": event.get("full_name", "Anurag Dangi"),
        "email": event.get("email", "your.email@example.com")
    }

    http = urllib3.PoolManager()
    response = http.request("POST", url, body=json.dumps(payload), headers=headers)

    return {
        "statusCode": response.status,
        "body": response.data.decode("utf-8")
    }
