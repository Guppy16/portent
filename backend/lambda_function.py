import json


def load_price():
    try:
        with open("btc_full_historical_4h.json", "r") as json_file:
            data = json.load(json_file)
    except Exception as e:
        data = None

    if data is None:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {"error": "Could not load data file during initialization"}
            ),
        }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(data),
    }


def load_predictions(event):

    try:
        with open("predictions.json", "r") as json_file:
            DATA = json.load(json_file)
    except Exception as e:
        DATA = None

    if DATA is None:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {"error": "Could not load data file during initialization"}
            ),
        }

    query_params = event.get("queryStringParameters") or {}
    date_param = query_params.get("date_string")

    if not date_param:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {"error": "Missing required query parameter 'date_string'"}
            ),
        }

    processed_output = DATA.get(date_param, {})
    if len(processed_output) > 0:
        processed_output = processed_output[0]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(processed_output),
    }


def lambda_handler(event, context):

    path = event.get("path", "")

    if path == "/price":
        return load_price()

    # default
    return load_predictions(event)


# def lambda_handler(event, context):

#     try:
#         with open("predictions.json", "r") as json_file:
#             DATA = json.load(json_file)
#     except Exception as e:
#         DATA = None

#     if DATA is None:
#         return {
#             "statusCode": 500,
#             "headers": {"Content-Type": "application/json"},
#             "body": json.dumps(
#                 {"error": "Could not load data file during initialization"}
#             ),
#         }

#     query_params = event.get("queryStringParameters") or {}
#     date_param = query_params.get("date_string")

#     if not date_param:
#         return {
#             "statusCode": 400,
#             "headers": {"Content-Type": "application/json"},
#             "body": json.dumps(
#                 {"error": "Missing required query parameter 'date_string'"}
#             ),
#         }

#     processed_output = DATA.get(date_param, {})
#     if len(processed_output) > 0:
#         processed_output = processed_output[0]

#     return {
#         "statusCode": 200,
#         "headers": {
#             "Content-Type": "application/json",
#             "Access-Control-Allow-Origin": "*",
#         },
#         "body": json.dumps(processed_output),
#     }
