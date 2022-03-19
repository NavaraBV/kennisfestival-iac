import os

from pymongo import MongoClient

from schemas.tasks import Task, TaskInDb


def __get_collection():
    uri = os.environ["MONGO_CONNECTION_STRING"]
    client = MongoClient(uri)
    return client.tasks.tasks


def list_tasks():
    db = __get_collection()
    tasks = [TaskInDb(id=str(task['_id']), **task).dict() for task in db.find({})]
    return tasks


def add_task(task):
    db = __get_collection()
    object_id = db.insert_one(task.dict()).inserted_id
    count = db.count_documents({})
    new_task = TaskInDb(**task.dict(), id=str(object_id))
    return new_task.dict()
