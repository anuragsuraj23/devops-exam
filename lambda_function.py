import json
import requests
import boto3
import os

def lambda_handler(event, context):
    # Extract environment variables
    subnet_id = os.environ.get("SUBNET_ID")
    full_name = os.environ.get("FULL_NAME", "Anurag Dangi")  # Update with your name
    email = os.environ.get("EMAIL", "your_email@example.com")  # Update with your email

    # API URL
    api_url = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    
    # API Headers
    headers = {
        "Content-Type": "application/json",
        "X-Siemens-Auth": "test"
    }

    # Payload
    payload = {
        "subnet_id": subnet_id,
        "full_name": full_name,
        "email": email
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response_data = response.json()
        
        # Log API response
        print("API Response:", response_data)
        
        return {
            "statusCode": response.status_code,
            "body": json.dumps(response_data)
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
