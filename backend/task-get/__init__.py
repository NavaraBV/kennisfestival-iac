import json
import logging

import azure.functions as func

from services.task_service import list_tasks

headers = {
    "Content-Type": "application/json",
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a GET request.")

    data = list_tasks()
    return func.HttpResponse(json.dumps(data), headers=headers)
