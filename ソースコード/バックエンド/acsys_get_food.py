import boto3
import json
from boto3.dynamodb.conditions import Attr,Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FoodCalorie')

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError

def lambda_handler(event, context):
    # TODO implement
    genre_ID = json.loads(event['body'])
    genre_ID = genre_ID.get('genre_ID')
    response = table.scan(
        FilterExpression = Attr('genre_ID').eq(genre_ID)
    )
    res = response['Items']
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(res,default = decimal_default_proc)
    }
