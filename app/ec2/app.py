import json
import os
import boto3

instance_id = os.environ['EC2_INSTANCE']
ec2_client = boto3.client('ec2')

def start(event, context):
    
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': f'Successfully started EC2 instance: {instance_id}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error starting EC2 instance: {str(e)}'
        }

def stop(event, context):

    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': f'Successfully stopped EC2 instance: {instance_id}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error stopping EC2 instance: {str(e)}'
        }