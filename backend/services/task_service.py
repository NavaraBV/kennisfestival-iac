import os

from pymongo import MongoClient

from schemas.tasks import Task


def __get_collection():
    uri = os.environ["MONGO_CONNECTION_STRING"]
    client = MongoClient(uri)
    return client.tasks.tasks


def list_tasks():
    db = __get_collection()
    tasks = [Task(**task).dict() for task in db.find({})]
    return tasks


def add_task(task):
    db = __get_collection()
    db.insert_one(task.dict())
    count = db.count_documents({})
    return {"message": "task added", "number of tasks": count}
