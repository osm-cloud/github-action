import boto3
import json

def lambda_handler(event, context):
    test = event["methodArn"]
    path = test.split("/")
    if path[1] == "v1":
        print("hello")
    else:
        print("Access Denied on Path")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from test-Lambda!')
    }