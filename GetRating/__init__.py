import logging
import json

import azure.functions as func

def main(req: func.HttpRequest, rateitems: func.DocumentList) -> str:
    logging.info('Python HTTP trigger function processed a request.')
    if not rateitems:
        logging.warning("ToDo item not found")
    else:
        logging.info("Found ToDo item, Description=%s",
                     rateitems[0]['timestamp'])

    #jsonString = json.dumps(rateitems, separators=(',',':'))
    jsonString = json.dumps({'id': rateitems[0]['id'], 'userId': rateitems[0]['userId'], 'productId': rateitems[0]['productId'], 'timestamp': rateitems[0]['timestamp'], 'locationName': rateitems[0]['locationName'], 'rating': rateitems[0]['rating'], 'userNotes': rateitems[0]['userNotes']}, indent=4, default=str)
    
    logging.info(jsonString)

    return func.HttpResponse(f"{jsonString}")
