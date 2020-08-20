import boto3
import json
from boto3.dynamodb.conditions import Attr,Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserManagement')

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    logout_token = body.get('account_token')
    logout_account = table.scan(
        FilterExpression = Attr('account_token').eq(logout_token)
    )
    print(logout_account)
    
    if not logout_account['Items']:
        response = {
            'isSuccess':False
        }
    else:
        user_id = logout_account['Items'][0].get('account_ID')
        table.update_item(
            Key = {'account_ID':user_id},
            UpdateExpression='set account_token = :token',
            ExpressionAttributeValues = {':token':''}
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
