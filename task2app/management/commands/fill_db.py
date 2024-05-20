from random import choices
from django.core.management.base import BaseCommand
from homework.task2app.models import Client

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "consequuntur cumque, delectus et illo iste maxime " \
        "Accusamus accusantium aut beatae consequatur 21" \
        "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Client_{i}', email=f'mail{i}@mail.ru')
            client.save()
