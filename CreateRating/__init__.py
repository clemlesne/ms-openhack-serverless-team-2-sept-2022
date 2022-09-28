import logging
import azure.functions as func
import requests
from uuid import UUID, uuid4
import json
from datetime import datetime


class DefaultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    # Get body from HttpRequest
    req_body = req.get_body()
    req_json = req.get_json()
    logging.info(req_body)

    # Get userId, rate and productId from HttpRequest
    userIdBody = req_json.get("userId")
    logging.info(userIdBody)
    productIdBody = req_json.get("productId")
    logging.info(productIdBody)
    ratingBody = req_json.get("rating")
    logging.info(ratingBody)

    # call api productId
    # response = requests.get("https://serverlessohapi.azurewebsites.net/api/GetProduct?productId=75542e38-563f-436f-adeb-f426f1dabb5c")
    queryProductId = {"productId": productIdBody}
    responseProduct = requests.get(
        "https://serverlessohapi.azurewebsites.net/api/GetProduct",
        params=queryProductId,
    )
    logging.info(responseProduct.json())

    # call api userId
    queryUserId = {"userId": userIdBody}
    responseUser = requests.get(
        "https://serverlessohapi.azurewebsites.net/api/GetUser", params=queryUserId
    )
    logging.info(responseUser.json())

    # timestamp
    today = datetime.utcnow()
    print("Today's date:", today)

    # validate rating
    ratingInt = int(ratingBody)
    if ratingInt >= 0 and ratingInt <= 5:
        logging.info("Rate valide")
    else:
        logging.info("Rate invalide")

    # generate uuid
    uuidOne = uuid4()
    logging.info(uuidOne)

    # create json object
    jsonString = json.dumps(
        {
            "id": uuidOne,
            "userId": userIdBody,
            "productId": productIdBody,
            "timestamp": today,
            "locationName": req_json.get("locationName"),
            "rating": ratingBody,
            "userNotes": req_json.get("userNotes"),
        },
        cls=DefaultEncoder,
    )
    logging.info(jsonString)

    if jsonString:
        doc.set(func.Document.from_json(jsonString))

    return func.HttpResponse(
        jsonString,
        mimetype="application/json",
        status_code=201,
    )
