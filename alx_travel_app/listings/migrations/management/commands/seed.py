from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.create(title='Sample Listing', description='This is a sample listing', price=100.00)
        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
