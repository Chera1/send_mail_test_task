# coding=utf-8
import datetime

import pytz
from django.core import mail
from django.template.loader import render_to_string

from mailganer.models import EmailsLog
from mailganer.utils import get_sub_data, get_emails_log
from main import settings
from main.celery_app import app


@app.task
def send_html_email(subject, template, context, recipients):
    html_message = render_to_string(template, context)
    return mail.send_mail(
        subject=subject,
        message="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        html_message=html_message,
    )


@app.task
def send_subscriber_notification(user):
    recipient = user.email
    send_html_email(
        subject="NewsLetter Subscription",
        template="notification.html",
        context={"user": user},
        recipients=[recipient],
    )


@app.task
def send_mass_mails(subject='NewsLetter Subscription'):
    data = get_sub_data()
    for user in data:
        send_html_email(subject=subject, template="notification.html", context={'user': user},
                        recipients=[user.email])


@app.task
def get_logs():
    data = get_emails_log()
    for item in data['items']:
        if item.get('reject'):
            EmailsLog.objects.update_or_create(reject_reason=item['reject']['reason'],
                                           message_id=item['message']['headers']['message-id'],
                                           status=item['event'],
                                           timestamp=datetime.datetime.fromtimestamp(item['timestamp'],
                                               tz=pytz.timezone(
                                                   settings.TIME_ZONE)
                                               ))
        elif item.get("recipient"):
            EmailsLog.objects.update_or_create(recipient=item['recipient'],
                                               message_id=item['message']['headers']['message-id'],
                                               status=item['event'],
                                               timestamp=datetime.datetime.fromtimestamp(item['timestamp'],
                                               tz=pytz.timezone(
                                                   settings.TIME_ZONE)
                                               ))
