import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        # Retrieve all items from the DynamoDB table
        response = table.scan()
        items = response.get('Items', [])
        
        return success_response('Items retrieved successfully', items)
        
    except Exception as e:
        return error_response(500, str(e))

def validate_data(data):
    required_fields = ['id']  # Modify this list based on your requirements
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

def success_response(message, result=None):
    response_body = {'message': 'Success', 'result': message}
    if result is not None:
        response_body['data'] = result
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response_body, default=decimal_encoder)
    }

def error_response(status_code, message):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Error', 'result': message})
    }

def decimal_encoder(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
