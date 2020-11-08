FROM alphacep/kaldi-vosk-server:latest 

RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

COPY ./worker /worker

WORKDIR /worker

RUN mkdir /worker/downloads

RUN chown -R nobody:nogroup /worker

RUN pip install -r requirements.txt

ENTRYPOINT celery -A tasks worker --loglevel=info
