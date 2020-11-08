from datetime import datetime
import os

import json

from vosk import KaldiRecognizer

import urllib.request
import uuid

SAMPLE_FREQUENCY = 16000
AUDIO_PATH = "./downloads"


def download_temp_file(url, dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    filename = os.path.join(dir_name, str(uuid.uuid4()))
    urllib.request.urlretrieve(url, filename=filename)
    return filename


def remove_temp_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def transcribe(model, audio_url):
    recognizer = KaldiRecognizer(model, SAMPLE_FREQUENCY)

    elapsed_time = None
    transcript = []

    audio_file = download_temp_file(audio_url, AUDIO_PATH)

    with open(audio_file, "rb") as f:
        start_time = datetime.now()

        f.read(44)  # skip header

        while True:
            data = f.read(2000)
            if len(data) == 0:
                break

            if recognizer.AcceptWaveform(data):
                words = json.loads(recognizer.Result())
                transcript.append(words)

        words = json.loads(recognizer.FinalResult())
        transcript.append(words)

        end_time = datetime.now()
        elapsed_time = end_time - start_time

    remove_temp_file(audio_file)

    transcript = [t for t in transcript if len(t["result"]) != 0]

    phrases = [t["text"] for t in transcript]

    transcription = " ".join(phrases)

    return {
        "elapsed_time": str(elapsed_time),
        "transcription": transcription,
    }
