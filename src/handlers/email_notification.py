import os
import boto3
# from botocore.vendored import requests
# import json
from src.helpers.email_helper import EmailHelper
from botocore.exceptions import ClientError

SENDER = "Finvoice Event Notifications <rohan@finvoice.co>"
CHARSET = "UTF-8"

def trigger(event, context):
    platform_url = os.environ['ENV_PLATFORM_URL'];
    platform_url = platform_url + '/' if not platform_url.endswith('/') else platform_url
    session_token = boto3.client('ssm').get_parameter(Name=os.environ['ENV_SESSION_TOKEN'], WithDecryption=True)["Parameter"]["Value"]
    analytics_url = platform_url + "analytics/1" # passing 1 sends email to all clients

    # response = requests.post(analytics_url, data={}, headers={"session-token": session_token, "tenant-token": "finvoice"})

    body_html = "<html><body><b>Testing sending of event notifications</b></body></html>"
    body_text = "Testing sending of event notifications"

    try:
        response = EmailHelper().send_mail(
            to_address=["rohan@finvoice.co"],
            email_html=body_html,
            email_text=body_text,
            subject="Finvoice Notification")

    except ClientError as e:
        return {
            'status': "Error sending email : " + e.response['Error']['Message'],
            'status_code': 400
        }
    else:
        return {
            'status': "Successfully sent email notification : " + response['MessageId'],
            'status_code': 200
        }