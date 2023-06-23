# coding=utf-8
import pytest

from main.tasks import send_mass_mails, send_subscriber_notification


@pytest.mark.django_db
def test_send_mass_mails(subscriber_factory, mailoutbox):
    s = subscriber_factory.create_batch(3)
    send_mass_mails()

    assert len(mailoutbox) == 3
    mail_to = [mail.to[0] for mail in mailoutbox]
    assert mail_to == [each.email for each in s]


@pytest.mark.django_db
def test_send_subscriber_notification(subscriber_factory, mailoutbox):
    sub = subscriber_factory.create()
    send_subscriber_notification(sub)

    assert len(mailoutbox) == 1
    mail_to = mailoutbox[0].to
    assert mail_to == [sub.email]
