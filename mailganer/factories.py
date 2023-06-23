import factory

from mailganer.models import Subscribers


class SubscriberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscribers

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    birthday = factory.Faker('date')
