import requests
import pickle


URL_API = "http://localhost:5000"


def rf():
    with open('tasks.bin', 'rb') as f:
        return pickle.load(f)


def check_task(task_id):
    response = requests.get(f"{URL_API}/check/{task_id}")

    response.raise_for_status()

    return response.content.decode()


tasks = rf()
status = [check_task(t) for t in tasks]

print(status)
