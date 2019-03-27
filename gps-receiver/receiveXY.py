from datetime import datetime
import json

def hello(event, context):
    body = {
        "message": "Your Lambda is working: " + str(datetime.now()),
        "inputEvent": event,
        "inputContext": context
    }

response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

return response
