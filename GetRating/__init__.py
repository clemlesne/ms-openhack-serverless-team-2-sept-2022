import azure.functions as func
import json
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class DefaultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class Rating(BaseModel):
    id: UUID
    userId: UUID
    productId: UUID
    timestamp: datetime
    locationName: str
    rating: int
    userNotes: str


def main(
    getHttpReq: func.HttpRequest, getByIdFromCosmosdb: func.DocumentList
) -> func.HttpResponse:
    ratings = []
    for data in getByIdFromCosmosdb:
        try:
            rating = Rating(**json.loads(data.to_json()))
            ratings.append(rating)
        except:
            pass

    rating = ratings[0].dict() if len(ratings) > 0 else None

    return func.HttpResponse(
        json.dumps(rating, cls=DefaultEncoder),
        mimetype="application/json",
        status_code=200,
    )
