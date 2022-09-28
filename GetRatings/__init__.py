import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, documents: func.DocumentList) -> str:
    logging.info('Python HTTP trigger function processed a request.')
    if not documents:
        logging.warning("ToDo item not found")
    else:
        logging.info("Found ToDo item, Description=%s",
                     documents[0]['timestamp'])
    jsonString = ""
    for document in documents:
        jsonString += json.dumps(document.to_json())

    return func.HttpResponse(f"{jsonString}")
