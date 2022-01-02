import os
from celery import Celery

celery = Celery("web", broker=os.environ["CELERY_BROKER_URL"], backend="rpc://")
