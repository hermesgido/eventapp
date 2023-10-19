from django.core.management.base import BaseCommand
from event.seed_data import seed_data

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        seed_data()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
