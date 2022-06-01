from csv import DictReader
import os

from django.core.management import BaseCommand
from django.db import OperationalError

from api_yamdb.settings import CSV_FILES_DIR
from users.models import UserProfile

ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для новой пустой
базы данных с таблицами"""

USERS_CSV_FILE = 'users.csv'


class Command(BaseCommand):
    print(f'Загрузка данных из {USERS_CSV_FILE}')

    def handle(self, *args, **options):

        try:
            if UserProfile.objects.exists():
                print(f'Данные из {USERS_CSV_FILE} уже загружены...выходим.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return
        except OperationalError:
            print('Импортируемая таблица не найдена.')
            return

        print(f'Загрузка {USERS_CSV_FILE}')

        users_path = os.path.join(CSV_FILES_DIR, USERS_CSV_FILE)
        for row in DictReader(open(users_path)):
            user = UserProfile(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            )
            user.save()
