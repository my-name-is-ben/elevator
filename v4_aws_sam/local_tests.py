# ==============================================================================
# The purpose of this file is to perform local testing before deploying to dev/prod.
# Each query is designed to simulate the 'event' object receive by the Lambda from the API Gateway.
# Time is limited, so the test cases are all manual.
# ==============================================================================

from elevator.app import lambda_handler
import json

# test requests to send to the lambda
# query = {
#   'resource': '/calc',
#   'httpMethod': 'POST',
#   'body': json.dumps({
#     "elevator_start": 4,
#     "floors": [1, 2, 3]
#   })
# }

query = {
  'resource': '/calc',
  'httpMethod': 'POST',
  'body': json.dumps({
    "elevator_start": 12,
    "floors": [27, 9, 27]
  })
}

# send the request
response = lambda_handler(query, '')

# print the response
print('statusCode: ', response['statusCode'])

response['body'] = json.loads(response['body'])

if isinstance(response['body'], list):
    for item in response['body']:
        print(json.dumps(item, indent=2))
else:
    print(json.dumps(response['body'], indent=2))

