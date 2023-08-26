import json
import boto3
from utils import utils

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        request_data = json.loads(event['body'])  # Parsing the JSON data from the request body
        utils.validate_data(request_data)
        
        id_value = request_data['id']
        
        if not is_exists(id_value):
            return utils.error_response(400, 'Item with the given id does not exist')
        
        delete_response = delete_item(id_value)
        return delete_response
        
    except Exception as e:
        return utils.error_response(500, str(e))

def is_exists(id_value):
    response = table.get_item(Key={'id': id_value})
    return 'Item' in response

def delete_item(id_value):
    response = table.delete_item(Key={'id': id_value})
    # Handle response or errors from DynamoDB if needed
    return utils.success_response('Item deleted successfully')