from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Добавление нового клиента."
    def handle(self, *args, **kwargs):
        client = Client(client_name='Ванинен Павел Андреевич', email='sdsd@hd.ru', password='27272', phone='839389238293', address='spb')
        client.save()
        self.stdout.write(f'{client}')

