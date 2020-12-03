import boto3
import uuid

a4b = boto3.client('alexaforbusiness')

def send_announcement(room_key, room_name, message, ttl):

    result = a4b.send_announcement(
        RoomFilters=[
            {
                "Key": room_key,
                "Values": [room_name],
            },
        ],
        Content={
                'TextList': [
                    {
                        'Locale': 'en-US',
                        'Value': message
                    },
                ]
        },
        TimeToLiveInSeconds = ttl,
        ClientRequestToken = str(uuid.uuid4())
    )
    return result

def lambda_handler(event, context):
    
    requestKey = event["headers"]["roomKey"]
    requestRoomContent = event["queryStringParameters"]["roomContent"]
    requestValue = event["body"]
    requestTtl = event["queryStringParameters"]["requestTtl"]


    send_announcement(room_key = requestKey, room_name = requestRoomContent, message = requestValue, ttl = requestTtl)

    return event

