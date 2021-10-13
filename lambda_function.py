# -*- coding: utf-8 -*-
import boto3
import json

def lambda_handler(event, context):

  input_event = {
    'repositoryName': 'MergeEventDetectiton',
    'source': 'develop01',
    'destination': 'develop03'
  }
  Payload = json.dumps(input_event)

  response = boto3.client('lambda').invoke(
    FunctionName='GetMergeConflict',
    InvocationType='RequestResponse',
    Payload=Payload
  )
  
  return json.loads(response['Payload'].read())