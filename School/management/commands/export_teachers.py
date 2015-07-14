from django.core import serializers
from django.core.management.base import BaseCommand
from School.models import Teacher


class Command(BaseCommand):
    help = 'Export teachers'

    def handle(self, *args, **options):
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()
        json_serializer.serialize(Teacher.objects.all())
        data = json_serializer.getvalue()

        with open("teachers.json", "w") as out:
            json_serializer.serialize(Teacher.objects.all(), stream=out)
