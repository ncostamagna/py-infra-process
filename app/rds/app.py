import json
import os
import boto3

db_instance = os.environ['DB_INSTANCE']
rds = boto3.client('rds')

def start(event, context):
    try:
        response = rds.start_db_instance(DBInstanceIdentifier=db_instance)
        return {
            'statusCode': 200,
            'body': f'Successfully paused RDS instance: {db_instance}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error pausing RDS instance: {str(e)}'
        }

def stop(event, context):
    try:
        response = rds.stop_db_instance(DBInstanceIdentifier=db_instance)
        return {
            'statusCode': 200,
            'body': f'Successfully paused RDS instance: {db_instance}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error pausing RDS instance: {str(e)}'
        }