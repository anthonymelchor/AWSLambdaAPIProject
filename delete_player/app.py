import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        request_data = json.loads(event['body'])  # Parsing the JSON data from the request body
        validate_data(request_data)
        
        id_value = request_data['id']
        
        if not is_exists(id_value):
            return error_response(400, 'Item with the given id does not exist')
        
        delete_response = delete_item(id_value)
        return delete_response
        
    except Exception as e:
        return error_response(500, str(e))

def validate_data(data):
    required_fields = ['id']  # You can add any additional required fields here
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

def is_exists(id_value):
    response = table.get_item(Key={'id': id_value})
    return 'Item' in response

def delete_item(id_value):
    response = table.delete_item(Key={'id': id_value})
    # Handle response or errors from DynamoDB if needed
    return success_response('Item deleted successfully')

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

