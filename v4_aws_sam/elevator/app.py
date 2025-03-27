import json
import logging


def lambda_handler(event, context):

    """
    Handles the routing of an api request, calculates the elevator travel time, and returns the response through api gateway.

    :param event: json object received from api gateway containing http request info
    :param context: json object received from api gateway containing additional context data
    :return: if function is successful, elevator sim results are returned. if an error occurs, error data is returned instead
    """

    try:
        # initialize logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # log the event
        logger.info(f'Request received: {event}')
        req_body = json.loads(event['body'])

        # variables
        TRAVEL_TIME = 10                                # single floor travel time
        total_travel_time = 0
        starting_floor = req_body['elevator_start']
        floor_list = req_body['floors']

        # add the starting floor to the floor list
        floor_list.insert(0, starting_floor)

        # iterate through the list to get the total_travel_time
        for i in range(len(floor_list) - 1):
            total_travel_time += abs(floor_list[i] - floor_list[i+1]) * TRAVEL_TIME

        # return elevator sim data
        return {
            "statusCode": 200,
            "body": json.dumps({
                "total_travel_time": total_travel_time,
                "floors_visited": floor_list
            }),
        }

    except Exception as ex:
        logger.error(f'Error in lambda_handler: {repr(ex)}')

        return {
            'statusCode': 400,
            'body': json.dumps(repr(ex))
        }
