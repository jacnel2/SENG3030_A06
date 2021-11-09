#FILE:      A06.PY
#COURSE:    SENG3030 - A06
#DATE:      2021-11-09
#PURPOSE:   Provides the backend that sends messages using Amazon's SNS
import boto3
import os

#PURPOSE:   Provides the backend that sends messages using Amazon's SNS
class Backend:
    #Secret keys so that we can send messages to the API endpoint, retrieved from memory
    ACCESS_KEY = os.environ.get("ACCESS_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")

    #Client to send the data with
    Client = boto3.client("sns", region_name="us-east-1",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )

    #PURPOSE:   Sends messages
    #PARAMS:    msg - message to send
    #RETURNS:   The response from sending the message
    def SendMsg(self, msg):
        response = self.Client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:667801258137:a06_test',
        Message = msg
        )
        return response