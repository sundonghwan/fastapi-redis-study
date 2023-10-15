# FastAPI 모듈 임포트
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

# Celery 요청 및 결과 수신을 위한 모듈 임포트
from config import celery_client
import uvicorn

from worker import test_msg

celery_app = celery_client('testCelery')
app = FastAPI()

def celery_on_message(body):
    print(body)

def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))

@app.post("/send")
async def send_msg(msg: str):
    task = test_msg.delay(msg)
    result = {"task_id": str(task)}
    print(task)
    return JSONResponse(result)

@app.get("/receive/{task_id}")
async def receive_msg(task_id: str):
    task = celery_app.AsyncResult(task_id)
    print(task.state)
    if task.on_ready(task.result):
        return {"result": task.get()}
    else:
        return {"result": "Not ready"}

if __name__ == "__main__":
    uvicorn.run("main:app")