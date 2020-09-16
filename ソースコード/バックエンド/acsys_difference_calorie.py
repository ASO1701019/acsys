import boto3
import json
import datetime
from boto3.dynamodb.conditions import Attr,Key
from decimal import Decimal

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError
    
def over24Hdatetime(year, month, day, hour, minute):

    #to minute
    minutes = int(hour)*60 + int(minute)

    dt = datetime.datetime(year=year, month=month, day=day)
    dt += datetime.timedelta(minutes=minutes)    

    return dt
    
dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('UserManagement')
intaked_table = dynamodb.Table('UserIntakedCalorie')
burned_table = dynamodb.Table('UserBurnedCalorie')
    
def lambda_handler(event, context):
    # TODO implement
    token = json.loads(event['body'])
    token = token.get('account_token')
    account_info = user_table.scan(
        FilterExpression = Attr('account_token').eq(token)
    )
    response = {}
    if not account_info['Items']:
        response['isSuccess'] = False
    else:
        account_ID = int(account_info['Items'][0].get('account_ID'))
        print(account_ID)
        print(type(account_ID))
        total_intaked = 0
        total_burned = 0
        today_intaked = 0
        today_burned = 0
        
        today = datetime.datetime.now()
        print(today)
        jpn = over24Hdatetime(today.year,today.month,today.day,today.hour+9,today.minute)
        print(jpn)
        jpn_today = jpn.year*10**4 + jpn.month*10**2 + jpn.day
        print(jpn_today)
        
        intakes = intaked_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID)
        )
        if not intakes['Items']:
            # response['total_intaked'] = 0
            response['today_intaked'] = 0
        else:
            for intake in intakes['Items']:
                total_intaked += int(intake['food_calorie'])
                if int(intake['add_date'])==jpn_today:
                    today_intaked += int(intake['food_calorie'])
            # response['total_intaked'] = total_intaked
            response['today_intaked'] = today_intaked
        
        burns = burned_table.scan(
            FilterExpression = Attr('account_ID').eq(account_ID)
        )
        if not burns['Items']:
            # response['total_burned'] = 0
            response['today_burned'] = 0
        else:
            for burn in burns['Items']:
                total_burned += int(burn['motion_calorie'])
                if int(burn['add_date'])==jpn_today:
                    today_burned += int(burn['motion_calorie'])
            # response['total_burned'] = total_burned
            response['today_burned'] = today_burned
        
        difference_calorie = total_burned - total_intaked
        response['difference_calorie'] = difference_calorie
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response,default = decimal_default_proc)
    }
    