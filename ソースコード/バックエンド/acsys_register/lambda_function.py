import json
import datetime
import boto3
from boto3.dynamodb.conditions import Attr

def over24Hdatetime(year, month, day, hour, minute):
    #to minute
    minutes = int(hour)*60 + int(minute)
    dt = datetime.datetime(year=year, month=month, day=day)
    dt += datetime.timedelta(minutes=minutes)    
    return dt

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('UserManagement')
        register = json.loads(event['body'])
        # regist_address = register.get('account_address')
        response = table.scan(
            FilterExpression = Attr('account_address').eq(register['account_address'])
        )
        items = response['Items']
        if not items:
            
            id_count = table.scan()['Count'] + 1
            register['account_ID'] = id_count
            
            today = datetime.datetime.now()
            jpn = over24Hdatetime(today.year,today.month,today.day,today.hour+9,today.minute)
            jpn_today = jpn.year*10**4 + jpn.month*10**2 + jpn.day
        
            register['regist_date'] = jpn_today
            print(register)
            
            table.put_item(Item = register)
            flg = {'isSuccess':True}
        else:
            raise Exception

    except Exception as e:
        flg = {
            'isSuccess':False,
            'message':str(e)
        }
        # raise e
    
    res = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(flg)
    }
    
    return  res