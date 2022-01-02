import time
import os
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks',
             broker=os.environ['CELERY_BROKER_URL'],
             backend='rpc://')


@app.task()
def process_order(data):
    logger.info('Got Order - Starting work ', data)
    data['order_status'] = '200'
    return data

