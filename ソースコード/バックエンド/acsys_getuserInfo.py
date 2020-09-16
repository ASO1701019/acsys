import boto3
import json
from boto3.dynamodb.conditions import Attr,Key
from decimal import Decimal

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserManagement')
    token = json.loads(event['body'])
    print(token)
    token = token.get('account_token')
    
    response = table.scan(
        FilterExpression = Attr('account_token').eq(token)
    )
    

    items = response['Items'][0]
    items.pop('account_token')
    items.pop('account_pass')
    items.pop('account_ID')
    items['isSuccess'] = True
    print(items)
    
    res = {
        'statusCode': 200,
        'headers':{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*',
        },
        'body': json.dumps(items,default = decimal_default_proc)
    }
    
    return res