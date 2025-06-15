from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.create(title='Beach House', description='Nice view.', price_per_night=120.00)
        Listing.objects.create(title='Mountain Cabin', description='Peaceful stay.', price_per_night=80.00)
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
