# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscribers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class EmailsLog(models.Model):
    recipient = models.EmailField()
    message_id = models.CharField(max_length=255)
    status = models.CharField(max_length=25)
    reject_reason = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
