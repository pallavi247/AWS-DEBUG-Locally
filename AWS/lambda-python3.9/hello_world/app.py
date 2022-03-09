import json

# import requests


def lambda_handler(event, context):
    first_name = event["first_name"]
    last_name = event["last_name"]
    message = event["message"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": f"{message} {first_name} {last_name}",
                #"message": "Hello World"
                # "location": ip.text.replace("\n", "")
            }
        ),
    }