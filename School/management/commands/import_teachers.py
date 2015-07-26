from django.core import serializers
from django.core.management.base import BaseCommand
from School.models import Teacher


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+')

    def handle(self, *args, **options):
        with open("teachers.json", "r") as data:
            for deserialized_object in serializers.deserialize("json", data, ignorenonexistent=True):
                    deserialized_object.save()


            
