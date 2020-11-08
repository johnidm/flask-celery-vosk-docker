FROM python:3.8-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG true

COPY ./api /api

WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 5000

RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
