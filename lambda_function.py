import json
import requests
import boto3

def lambda_handler(event, context):
    subnet_id = event.get("subnet_id", "subnet-default")
    headers = {
        "X-Siemens-Auth": "test",
        "Content-Type": "application/json"
    }
    payload = {
        "subnet_id": subnet_id,
        "full_name": "Anurag Dangi",
        "email": "anurag@example.com"
    }
    response = requests.post("https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data", 
                             headers=headers, json=payload)
    
    return {
        "statusCode": response.status_code,
        "body": json.loads(response.text)
    }
