# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import re

from .models import Subscribers
from main.tasks import send_subscriber_notification, send_mass_mails


def subscribe(request):
    """
    Creating users to db and sending them notification mail.
    :param request: request from ajax.
    :return: response of request or back at main page.
    """
    if request.method == "POST":
        post_data = request.POST.copy()
        email = post_data.get("userEmail", None)
        username = post_data.get("userName", None)
        last_name = post_data.get("userLastName", None)
        first_name = post_data.get("userFirstName", None)
        birthday = post_data.get("userBirthday", None)
        subscribed_user = Subscribers.objects.create(email=email,
                                                     username=username,
                                                     last_name=last_name,
                                                     first_name=first_name,
                                                     birthday=birthday)
        send_subscriber_notification(subscribed_user)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'index.html')


def validate_email(request):
    """
    func is validating entering email address by user.
    :param request: request with email address.
    :return: response.
    """
    email = request.POST.get("userEmail", None)
    try:
        subscriber = Subscribers.objects.get(email=email)
    except Subscribers.DoesNotExist:
        subscriber = None
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif subscriber:
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res


def mass_mailing(request):
    """
    page with one function - creating mass mailing newsletters all users from db.
    :param request: request with subject of newsletters.
    :return: response of request or back at main page.
    """
    if request.method == 'POST':
        post_data = request.POST.copy()
        subject = post_data.get("subject", None)
        send_mass_mails(subject)
        res = JsonResponse({'msg': 'Thanks. Mass mailing Successfully!'})
        return res
    return render(request, 'mass_mailing.html')

