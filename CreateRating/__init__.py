import logging

import azure.functions as func
import requests
from datetime import datetime

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    request_body = req.get_body()
    logging.info(request_body)
    userIdBody = request_body["userId"]
    logging.info(userIdBody)

    #call api productId
    response = requests.get("https://serverlessohapi.azurewebsites.net/api/GetProduct?productId=75542e38-563f-436f-adeb-f426f1dabb5c")
    print(response.json()["productId"])

    #call api userId
    response = requests.get("https://serverlessohapi.azurewebsites.net/api/GetUser?userId=cc20a6fb-a91f-4192-874d-132493685376")
    print(response.json()["userId"])

    #timestamp
    today = datetime.utcnow()
    print("Today's date:", today)

    #if request_body:
        #doc.set(func.Document.from_json(request_body))

    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
