import boto3
import json
from boto3.dynamodb.conditions import Attr,Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserManagement')

def lambda_handler(event, context):
    login_array = json.loads(event['body'])
    print(login_array)
    login_address = login_array.get('account_address')
    login_password = login_array.get('account_pass')
    regist_token = login_array.get('account_token')
    print(login_address , login_password)
    
    response = table.scan(
        FilterExpression=Attr('account_address').eq(login_address) & Attr('account_pass').eq(login_password)
    )
    
    print(response)
    # items = response['Items'][0]
    # print(items)
    
    if not response['Items']:
        result = False
        flg={'isSuccess':result}
        res = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps(flg)
        }
        return res
    else:
        result = True
        items = response['Items'][0]
        print(type(regist_token))
        user_id = int(items.get('account_ID'))
        print(user_id)
        table.update_item(
            Key = {'account_ID':user_id},
            UpdateExpression='set account_token = :token',
            ExpressionAttributeValues = {':token':regist_token}
        )
        flg={'isSuccess':result}
        res = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps(flg)
        }
        return res