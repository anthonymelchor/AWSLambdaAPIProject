import json
import boto3
from utils import utils

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        id_value = event['queryStringParameters'].get('id')

        if id_value is None:
            return utils.error_response(400, 'Missing id in the request')
        
        if not id_exists(id_value):
            return utils.error_response(404, 'Player not found')

        player = get_player_by_id(id_value)

        return player        
        
    except Exception as e:
        return utils.error_response(500, str(e))

def id_exists(player_id):
    response = table.get_item(Key={'id': player_id})
    return 'Item' in response

def get_player_by_id(player_id):
    player_response = table.get_item(Key={'id': player_id})
    player = player_response.get('Item')

    return utils.success_response('Player found successfully', player)