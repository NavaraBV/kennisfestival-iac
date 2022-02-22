import json
import logging
import os
from enum import Enum

import azure.functions as func
from pydantic import ValidationError, BaseModel
from pymongo import MongoClient

headers = {
    "Content-Type": "application/json",
}


class StatusEnum(str, Enum):
    new = "new"
    completed = "completed"


class Task(BaseModel):
    task: str
    assignee: str
    status: StatusEnum


class TaskInDb(Task):
    id: str


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a POST request.")

    uri = os.environ["MONGO_CONNECTION_STRING"]
    client = MongoClient(uri)
    db = client.tasks.tasks

    try:
        task = Task(**req.get_json())
    except ValidationError as v:
        return func.HttpResponse(v.json(), headers=headers, status_code=412)

    object_id = db.insert_one(task.dict()).inserted_id
    new_task = TaskInDb(**task.dict(), id=str(object_id))

    return func.HttpResponse(json.dumps(new_task.dict()), headers=headers, status_code=201)
