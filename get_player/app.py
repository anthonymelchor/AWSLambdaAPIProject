import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        id_value = event['queryStringParameters'].get('id')
        
        if id_value is None:
            return error_response(400, 'Missing id in the request')
        
        if not id_exists(id_value):
            return error_response(404, 'Player not found')

        player = get_player_by_id(id_value)

        return player        
        
    except Exception as e:
        return error_response(500, str(e))

def id_exists(player_id):
    response = table.get_item(Key={'id': player_id})
    return 'Item' in response

def get_player_by_id(player_id):
    player_response = table.get_item(Key={'id': player_id})
    player = player_response.get('Item')

    return success_response('Player found successfully', player)

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

