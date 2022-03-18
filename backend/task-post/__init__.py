import json
import logging

import azure.functions as func
from pydantic import ValidationError

from schemas.tasks import Task
from services.task_service import add_task


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a POST request.")

    try:
        task = Task(**req.get_json())
    except ValidationError as v:
        return func.HttpResponse(
            v.json(), headers={"content-type": "application/json"}, status_code=412
        )

    data = add_task(task)
    return func.HttpResponse(
        json.dumps(data), headers={"content-type": "application/json"}
    )
