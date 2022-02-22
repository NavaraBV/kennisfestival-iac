import json
import logging
import os
from enum import Enum

import azure.functions as func
from pydantic import BaseModel
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
    logging.info("Python HTTP trigger function processed a GET request.")

    uri = os.environ["MONGO_CONNECTION_STRING"]
    client = MongoClient(uri)
    db = client.tasks.tasks
    tasks = [TaskInDb(id=str(task['_id']), **task).dict() for task in db.find({})]

    return func.HttpResponse(json.dumps(tasks), headers=headers)
