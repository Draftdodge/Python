from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Добавление нового клиента."

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='ФИО клиента')
        parser.add_argument('-e', '--email', type=str, help='Email клиента')
        parser.add_argument('-pwd', '--password', type=str, help='Пароль')
        parser.add_argument('-p', '--phone', type=str, help='Телефон')
        parser.add_argument('-a', '--address', type=str, help='Адрес')

    def handle(self, *args, **kwargs):
        client_name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        client = Client(client_name=client_name, email=email, password=password, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')

