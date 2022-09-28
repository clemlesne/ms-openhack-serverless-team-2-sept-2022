import logging
import azure.functions as func
import nest_asyncio
from uuid import UUID, uuid4
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field

from app.__init__ import version


class Rating(BaseModel):
    rating_id: UUID
    user_id: UUID
    product_id: UUID
    location_name: str
    rating: int = Field(gt=0, lt=5)
    user_notes: str


app = FastAPI()
nest_asyncio.apply()


@app.get("/ratings/")
async def get_rating():
    return []


@app.get("/ratings/{rating_id}")
async def get_rating(rating_id: UUID):
    return {
        "rating_id": rating_id,
    }


@app.post("/ratings/")
async def create_rating(rating: Rating):
   return rating


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
