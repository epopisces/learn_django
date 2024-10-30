# pxcp/management/commands/populate_items.py
from django.core.management.base import BaseCommand
from pxcp.models import Item

class Command(BaseCommand):
    help = 'Populate the database with sample items'

    def handle(self, *args, **kwargs):
        items = [
            {'name': 'Verisimilitude', 'description': 'the appearance of being true or real.', 'link': '/'},
            {'name': 'Highfalutin', 'description': 'pompous or pretentious', 'link': '/'},
            {'name': 'Highborn', 'description': 'having noble parents', 'link': '/admin_dashboard/'},
            # Add more items as needed
        ]
        for item in items:
            Item.objects.create(**item)
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample items'))