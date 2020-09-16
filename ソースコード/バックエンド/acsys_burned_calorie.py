import boto3
import json
from boto3.dynamodb.conditions import Attr,Key

dynamodb = boto3.resource('dynamodb')
burn_table = dynamodb.Table('UserBurnedCalorie')
user_table = dynamodb.Table('UserManagement')

def lambda_handler(event, context):
    # TODO implement
    try:
        body = json.loads(event['body'])
        scan_token = body.get('account_token')
        varid_account = user_table.scan(
            FilterExpression=Attr('account_token').eq(scan_token)
            )
        # print(varid_account)
        
        if not varid_account['Items']:
            response = {
                'isSuccess':False
            }
        else:
            user_ID = varid_account['Items'][0].get('account_ID')
            # add_date = body.get('add_date')
            id_count = burn_table.scan()['Count']
            
            for record in body['data']:
                id_count += 1
                post_data = {
                    'burned_ID':id_count,
                    'account_ID':user_ID,
                    'add_date':record['add_date'],
                    'motion_name':record['motion_name'],
                    'motion_calorie':record['motion_calorie']
                }
                # print(post_data)
                burn_table.put_item(Item = post_data)
                
            response = {
                'isSuccess':True
            }
    except Exception as e:
        print('error')
        response = {
            'isSuccess':False,
            'error':str(e)
        }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response)
    }