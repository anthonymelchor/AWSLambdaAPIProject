import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        validate_data(data)
        
        id_value = data['id']
        
        if is_duplicate(id_value):
            return error_response(400, 'Item with the same id already exists')
        
        insert_item(data)
        return success_response('Item inserted successfully')
        
    except Exception as e:
        return error_response(500, str(e))

def validate_data(data):
    required_fields = ['id']  # Modify this list based on your requirements
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

def is_duplicate(id_value):
    response = table.get_item(Key={'id': id_value})
    return 'Item' in response

def insert_item(item):
    response = table.put_item(Item=item)
    # Handle response or errors from DynamoDB if needed

def success_response(message):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Success', 'result': message })
    }

def error_response(status_code, message):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': 'Error', 'result': message})
    }
