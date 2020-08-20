import boto3
import json
from boto3.dynamodb.conditions import Attr,Key
from decimal import Decimal

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError
    
dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('UserManagement')
intaked_table = dynamodb.Table('UserIntakedCalorie')
burned_table = dynamodb.Table('UserBurnedCalorie')

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    token = body.get('account_token')
    account_info = user_table.scan(
        FilterExpression = Attr('account_token').eq(token)
    )
    response = {}
    if not account_info['Items']:
        response['isSuccess'] = False
    else:
        account_ID = int(account_info['Items'][0].get('account_ID'))
        add_date = body.get('add_date')
        intaked_records = intaked_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID) & Attr('add_date').eq(add_date)
        )
        burned_records = burned_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID) & Attr('add_date').eq(add_date)
        )
        response['intaked'] = intaked_records['Items']
        response['burned'] = burned_records['Items']
        # print(intaked_records)
        # print(burned_records)
        print(response)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response,default = decimal_default_proc)
    }
