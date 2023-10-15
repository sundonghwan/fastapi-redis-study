# 환경변수 호출을 위한 os 모듈
import os

# 중요 데이터를 env파일로 관리하기위한 모듈
from dotenv import load_dotenv

# 워커 역활을 할 celery 모듈
from celery import Celery

load_dotenv()
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DATABASE = os.getenv("REDIS_DATABASE")

def celery_client(app_name):
    redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

    celery = Celery(app_name,
                    backend=redis_url,
                    broker=redis_url)

    return celery