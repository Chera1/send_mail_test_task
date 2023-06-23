# coding=utf-8
import requests

from mailganer.models import Subscribers
from main import settings
import json


def get_sub_data():
    subscribers = Subscribers.objects.all()
    return subscribers


def get_emails_log():
    data = requests.get('https://api.mailgun.net/v3/%s/events' % settings.MAILGUN_SERVER_NAME,
                        auth=('api', settings.MAILGUN_ACCESS_KEY))
    return json.loads(data.content)
