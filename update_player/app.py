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
        
        update_response = update_item(request_data)
        return update_response
        
    except Exception as e:
        return utils.error_response(500, str(e))

def is_exists(id_value):
    response = table.get_item(Key={'id': id_value})
    return 'Item' in response

def update_item(data):
    id_value = data.get('id')
    
    attributes_to_update = {key: value for key, value in data.items() if key != 'id'}
    
    if not attributes_to_update:
        error_message = 'No attributes to update'
        return utils.error_response(400, error_message)
    

    update_expression_parts = [f'#{key} = :{key}' for key in attributes_to_update]
    update_expression = "set " + ", ".join(update_expression_parts)
    
    expression_attribute_values = {f':{key}': value for key, value in attributes_to_update.items()}
    expression_attribute_names = {f'#{key}': key for key in attributes_to_update}
    
    response = table.update_item(
        Key={'id': id_value},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names
    )
    # Handle response or errors from DynamoDB if needed
    
    return utils.success_response('Item updated successfully')