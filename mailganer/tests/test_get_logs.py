# coding=utf-8
import pytest

from mailganer.models import EmailsLog
from main.tasks import get_logs


@pytest.mark.django_db
def test_get_logs(subscriber_factory):
    initial_count = EmailsLog.objects.count()
    subscriber_factory.create_batch(3)
    get_logs()
    assert initial_count == 0
    assert EmailsLog.objects.count() >= 3
