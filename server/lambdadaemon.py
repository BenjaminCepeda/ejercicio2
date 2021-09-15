import time
import logging
import requests
import json

from django.http import HttpResponse
from .models import Dato


def start_lambda_query(request):
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    # y = json.dumps(list(map(lambda x: get_data(), range(3))))
    r = lambda x, y: get_data(x, y)
    r(15, 60)   # intentos = 15 sleep = 60
    return HttpResponse("Start lambda Query")


def get_data(n, t):
    query_data = list({})
    url = 'https://dweet.io:443/get/latest/dweet/for/thecore'
    webhook_url = 'https://webhook.site/4ed54cff-41ba-423e-9f46' \
                  '-b2c87408daf9 '
    for i in range(n):
        data = requests.get(url, timeout=5)
        if data.status_code == 200:
            query_data.append(save_data(data.json()))
        time.sleep(t)
    dct = {"ResulSet": query_data}
    logging.debug("get_data call webhook")
    logging.debug(json.dumps(dct))
    requests.post(webhook_url, data=json.dumps(query_data),
                  headers={'Content-Type': 'application/json'})
    return query_data


def save_data(j):
    """
    logging.debug("Save data %s" % (datetime.datetime.now()))
    logging.debug(j['with'][0]['content']['temperature'])
    logging.debug(j['with'][0]['content']['humidity'])
    """
    d = Dato(temperature=j['with'][0]['content']['temperature'],
             humidity=j['with'][0]['content']['humidity'])
    d.save()
    return {'temperature': j['with'][0]['content']['temperature'], 'humidity':
        j['with'][0]['content']['humidity']}


