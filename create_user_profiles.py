# create_users.py
import random
from faker import Faker
from django.core.management.base import BaseCommand
from myapp.models import UserProfile

fake = Faker()

class Command(BaseCommand):
    help = 'Create 1000 users with usernames and mobile numbers'

    def handle(self, *args, **options):
        existing_mobile_numbers = set(UserProfile.objects.values_list('mobile_number', flat=True))

        for _ in range(1000):
            username = fake.user_name()
            mobile_number = self.generate_unique_mobile(existing_mobile_numbers)

            UserProfile.objects.create(
                username=username,
                mobile_number=mobile_number,
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 1000 users.'))

    def generate_unique_mobile(self, existing_mobile_numbers):
        mobile_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])

        while mobile_number in existing_mobile_numbers:
            mobile_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])

        existing_mobile_numbers.add(mobile_number)
        return mobile_number
