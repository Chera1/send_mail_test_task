# coding=utf-8
import pytest

from mailganer.utils import get_sub_data


@pytest.mark.django_db
def test_get_sub_data(subscriber_factory):
    subscriber_factory.create_batch(10)
    assert len(get_sub_data()) == 10
