import requests
import pickle


URL_API = "http://localhost:5000"


def wf(tasks):
    with open('tasks.bin', 'wb') as f:
        pickle.dump(tasks, f)


def transcribe(url):
    data = {
        "url": url
    }

    response = requests.post(f"{URL_API}/transcription/", json=data)

    response.raise_for_status()

    return response.content.decode()


url = "https://raw.githubusercontent.com/johnidm/kaldi-asr-architeture/master/audio.wav"

tasks = [transcribe(url) for _ in range(0, 10)]

wf(tasks)
