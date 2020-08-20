import boto3
import json
from boto3.dynamodb.conditions import Attr,Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserManagement')

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    token = body.get('account_token')
    update_account = table.scan(
        FilterExpression = Attr('account_token').eq(token)
    )

    if not update_account['Items']:
        response = {
            'isSuccess':False
        }
        
    else:
        user_id = update_account['Items'][0].get('account_ID')
        
        # weight
        
        user_weight = int(update_account['Items'][0].get('account_weight'))
        update_weight = body.get('account_weight')
        if user_weight != update_weight:
            table.update_item(
                Key = {'account_ID':user_id},
                UpdateExpression='set account_weight = :weight',
                ExpressionAttributeValues = {':weight':update_weight}
            )
            print('weight update')
        
        # height
        
        user_height = int(update_account['Items'][0].get('account_height'))
        update_height = body.get('account_height')
        if user_height != update_height:
            table.update_item(
                Key = {'account_ID':user_id},
                UpdateExpression='set account_height = :height',
                ExpressionAttributeValues = {':height':update_height}
            )
            print('height update')
        
        # level
        
        user_level = int(update_account['Items'][0].get('account_level'))
        update_level = body.get('account_level')
        if user_level != update_level:
            table.update_item(
                Key = {'account_ID':user_id},
                UpdateExpression='set account_level = :level',
                ExpressionAttributeValues = {':level':update_level}
            )
            print('level update')
        
        # address
        
        # user_address = update_account['Items'][0].get('account_address')
        # update_address = body.get('account_address')
        # if user_address != update_address:
        #     table.update_item(
        #         Key = {'account_ID':user_id},
        #         UpdateExpression='set account_address = :address',
        #         ExpressionAttributeValues = {':address':update_address}
        #     )
        #     print('height update')
            
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