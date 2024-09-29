import json
import os

def handler(event, context):
    db_instance = os.environ['DB_INSTANCE']
    rds = boto3.client('rds')

    try:
        response = rds_client.stop_db_instance(DBInstanceIdentifier=db_instance_identifier)
        return {
            'statusCode': 200,
            'body': f'Successfully paused RDS instance: {db_instance_identifier}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error pausing RDS instance: {str(e)}'
        }
