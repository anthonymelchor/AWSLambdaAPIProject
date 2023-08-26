import json
import boto3
from utils import utils

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tennis_player')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        # Retrieve all items from the DynamoDB table
        response = table.scan()
        items = response.get('Items', [])
        
        return utils.success_response('Items retrieved successfully', items)
        
    except Exception as e:
        return utils.error_response(500, str(e))