# Docker Flask Celery Vosk

A basic Docker Compose template for orchestrating a Flask application, Celery queue & a Vosk speech recognition toolkit

### Download pré-treined model

```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip && mv vosk-model-small-pt-0.3.zip ./worker && unzip ./worker/vosk-model-small-pt-0.3.zip -d ./worker
```

### Build and launch

Basic build:
```bash
docker-compose up -d --build
```

To add more workers:
```bash
docker-compose up -d --scale worker=5 --no-recreate
```

To shut down:

```bash
docker-compose down
```

### References

- https://gitlab.com/sfcarroll/flask-celery-docker
- https://github.com/alphacep
