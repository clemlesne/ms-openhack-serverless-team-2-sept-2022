import logging

import azure.functions as func
import requests
from datetime import datetime
import uuid
import json

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #Get body from HttpRequest
    request_body = req.get_body()
    logging.info(request_body)

    #Get userId, rate and productId from HttpRequest
    userIdBody = req.get_json().get('userId')
    logging.info(userIdBody)
    productIdBody = req.get_json().get('productId')
    logging.info(productIdBody)
    ratingBody = req.get_json().get('rating')
    logging.info(ratingBody)
    
    #call api productId
    #response = requests.get("https://serverlessohapi.azurewebsites.net/api/GetProduct?productId=75542e38-563f-436f-adeb-f426f1dabb5c")
    queryProductId = {'productId':productIdBody}
    responseProduct = requests.get('https://serverlessohapi.azurewebsites.net/api/GetProduct', params=queryProductId)
    logging.info(responseProduct.json())

    #call api userId
    queryUserId = {'userId':userIdBody}
    responseUser = requests.get('https://serverlessohapi.azurewebsites.net/api/GetUser', params=queryUserId)
    logging.info(responseUser.json())

    #timestamp
    today = datetime.utcnow()
    print("Today's date:", today)

    #validate rating
    ratingInt = int(ratingBody)
    if ratingInt >=0 and ratingInt <=5:
        logging.info("Rate valide")
    else:
        logging.info("Rate invalide")

    #generate uuid
    uuidOne = uuid.uuid1()
    logging.info(uuidOne)

    #create json object
    jsonString = json.dumps({'id': uuidOne, 'userId': userIdBody, 'productId': productIdBody, 'timestamp': today, 'locationName': req.get_json().get('locationName'), 'rating': ratingBody, 'userNotes': req.get_json().get('userNotes')}, indent=4, default=str)
    logging.info(jsonString)

    if jsonString:
        doc.set(func.Document.from_json(jsonString))

    return func.HttpResponse(f"{jsonString}")
