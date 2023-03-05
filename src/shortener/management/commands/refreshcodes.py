from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrURL


class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_codes()