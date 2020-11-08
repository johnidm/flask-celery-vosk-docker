import os
import time

from celery import Celery
from celery.utils.log import get_task_logger
from vosk import Model, KaldiRecognizer

from helpers import transcribe

logger = get_task_logger(__name__)


CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


MODEL_PATH = "./vosk-model-small-pt-0.3"


model = Model(MODEL_PATH)


@celery.task(name='tasks.transcription')
def transcription(url: str) -> int:
    logger.info('[task] transcription:' + url)
    return transcribe(model, url)
