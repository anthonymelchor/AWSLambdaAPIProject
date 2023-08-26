import json
import boto3
from utils import utils

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        utils.validate_data(data)
        
        id_value = data['id']
        
        if is_duplicate(id_value):
            return utils.error_response(400, 'Item with the same id already exists')
        
        insert_item(data)
        return utils.success_response('Item inserted successfully')
        
    except Exception as e:
        return utils.error_response(500, str(e))

def is_duplicate(id_value):
    response = table.get_item(Key={'id': id_value})
    return 'Item' in response

def insert_item(item):
    response = table.put_item(Item=item)
    # Handle response or errors from DynamoDB if needed