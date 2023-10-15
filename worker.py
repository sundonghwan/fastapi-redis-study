import celery

from config import celery_client
from celery import shared_task
from fastapi.responses import JSONResponse

@shared_task
def test_msg(msg):
    try:
        print(msg)
        result_data = {"success": msg}
        return result_data

    except Exception as e:
        return {"Fail": str(e)}
#
# def main():
#     celery_app.worker_main(argv=["worker", "--loglevel=info"])
#
# if __name__ == "__main__":
#     main()