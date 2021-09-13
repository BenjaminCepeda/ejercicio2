import time
import threading
import logging
import requests
import datetime

from django.http import HttpResponse
from .models import Dato


def start_lambda_daemon(request):
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    deamon_thread = threading.Thread(name='lambdadaemon', target=run(),
                                     daemon=True)
    deamon_thread.start()
    return HttpResponse("Start lambda Daemon")


def run():
    logging.debug('Running deamon')
    url = 'https://dweet.io:443/get/latest/dweet/for/thecore'
    try:
        i = 0
        while i < 15:
            logging.debug('Finding data ...' + str(i))
            data = requests.get(url, timeout=5)
            if data.status_code == 200:
                # logging.debug(data.json())
                elements = data.json()
                save_data(elements)
            i = i + 1
            time.sleep(60)
    except requests.exceptions.HTTPError as errh:
        logging.debug(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.debug(errc)
    except requests.exceptions.Timeout as errt:
        logging.debug(errt)
    except requests.exceptions.RequestException as err:
        logging.debug(err)
    logging.debug('Exiting deamon')


def save_data(j):
    logging.debug(datetime.datetime.now())
    logging.debug(j['with'][0]['content']['temperature'])
    logging.debug(j['with'][0]['content']['humidity'])
    d = Dato(temperature=j['with'][0]['content']['temperature'],
             humidity=j['with'][0]['content']['humidity'])
    d.save()
