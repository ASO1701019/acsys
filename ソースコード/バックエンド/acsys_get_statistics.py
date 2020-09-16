import boto3
import json
import datetime
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
        year = body.get('year')
        lower_year = int(year * 10 ** 4)
        upper_year = int(year * 10 ** 4 + 1231)
        total_intaked = [0,0,0,0,0,0,0,0,0,0,0,0]
        total_burned = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        intaked_records = intaked_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID) & Attr('add_date').between(lower_year,upper_year)
        )
        print(intaked_records)
        for intaked_record in intaked_records['Items']:
            date = int(intaked_record.get('add_date'))
            month = int((date - lower_year) / 10 ** 2)
            total_intaked[month-1] += int(intaked_record.get('food_calorie'))
        print(total_intaked)
        
        burned_records = burned_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID) & Attr('add_date').between(lower_year,upper_year)
        )
        print(burned_records)
        for burned_record in burned_records['Items']:
            date = int(burned_record.get('add_date'))
            month = int((date - lower_year) / 10 ** 2)
            total_burned[month-1] += int(burned_record.get('motion_calorie'))
        print(total_burned)
        
        response = {
            'isSuccess':True,
            'intaked':total_intaked,
            'burned':total_burned,
        }
        
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response,default = decimal_default_proc)
    }
    