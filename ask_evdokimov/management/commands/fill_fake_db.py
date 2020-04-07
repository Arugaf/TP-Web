from django.core.management.base import BaseCommand
from ask_evdokimov.models import *
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых постов')


    def handle(self, *args, **kwargs):
            total = kwargs['total']
            for i in range(1, total):
                u = User.objects.create_user('usernamenew' + str(i))
                Question.objects.create(title='NewTitle' + str(i), rating=10, auto=u)