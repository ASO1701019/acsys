import boto3
import json
from boto3.dynamodb.conditions import Attr,Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserIntakedCalorie')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    delete_ID = body.get('intaked_ID')
    
    table.update_item(
        Key = {'intaked_ID':delete_ID},
        UpdateExpression='set valid_flg = :flg',
        ExpressionAttributeValues = {':flg':0}
    )
    
    response = {
        'isSuccess':True
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response)
    }