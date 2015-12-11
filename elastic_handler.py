import requests
from time import sleep


def sendJson(job_objects):
    for counter, job in enumerate(job_objects):
        r = requests.post('http://104.155.89.25:5514', str(job))
        print("STATUS=" + str(r.status_code))
        sleep(0.2)

