# coding=utf-8
import pytest
from mailganer.models import Subscribers, EmailsLog
from mailganer.utils import get_sub_data
import uuid


@pytest.mark.django_db
def test_subscribers():
    Subscribers.objects.create(username='test', email='test@test.ru')
    assert get_sub_data().count() == 1


@pytest.mark.django_db
def test_emails_log():
    EmailsLog.objects.create(recipient='test@test.ru', message_id=uuid.uuid4())
    assert EmailsLog.objects.all().count() == 1
