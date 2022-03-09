import json
import boto3
import logging



logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')


def lambda_handler(event, context):
    
    #url = generate_presigned_url(
    #    s3, 'get_object', {'Bucket': 'document-objectstore', 'Key': event['object_key']}, 1000)
    print('Fetching object from S3')
    response = s3.get_object(Bucket='document-objectstore', Key=event['object_key'])
    file_content=response['Body'].read()
    content_type=response['ContentType']
    return {
        "statusCode": 200,
        "body": file_content,
        "content-type":content_type
        }
    

def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
    """
    Generate a presigned Amazon S3 URL that can be used to perform an action.

    :param s3_client: A Boto3 Amazon S3 client.
    :param client_method: The name of the client method that the URL performs.
    :param method_parameters: The parameters of the specified client method.
    :param expires_in: The number of seconds the presigned URL is valid for.
    :return: The presigned URL.
    """
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
        logger.info("Got presigned URL: %s", url)
    except Exception as err:
        logger.error ("Error -"+str(err))
        logger.exception(
            "Couldn't get a presigned URL for client method '%s'.", client_method)
        raise
    return url