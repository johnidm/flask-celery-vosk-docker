import os
from flask import Flask, request, jsonify
from worker import celery
import celery.states as states
import logging

app = Flask(__name__)

ROLLBAR_KEY = os.environ.get('ROLLBAR_KEY')
ROLLBAR_APP = os.environ.get('ROLLBAR_APP')

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route('/')
def index():
    app.logger.info('[route] /')
    return "<h1>Vosk - Speech To Text - Online </h1>"


@app.route('/transcription/', methods=['POST'])
def transcription() -> str:
    content = request.json
    
    url = content['url']
    app.logger.info('[route] /transcription/' + url)
    
    task = celery.send_task('tasks.transcription', args=[url], kwargs={})
    return task.id, 201


@app.route('/check/<string:task_id>', methods=['GET'])
def check_task(task_id: str) -> str:
    app.logger.info('[route] /check/' + task_id)
    res = celery.AsyncResult(task_id)

    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
