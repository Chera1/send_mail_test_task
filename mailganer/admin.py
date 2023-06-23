# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Subscribers, EmailsLog


@admin.register(Subscribers)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('username',)

    search_fields = ('username', 'id')


@admin.register(EmailsLog)
class EmailsLogAdmin(admin.ModelAdmin):
    list_display = ('message_id',)

    search_fields = ('recipient', 'message_id', 'status')
