import os, json
from django.core.management.base import BaseCommand, CommandError
from django_communes.models import Commune
from os.path import abspath, dirname

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        path = os.path.join(dirname(__file__), "data/")
        files = [
                x for x in os.listdir(path)
                if os.path.isfile(os.path.join(path, x))
            ]
        if ".DS_Store" in files:
            files.remove(".DS_Store")
        for file in files:
            path_file = "{}{}".format(path, file)
            with open(path_file, newline='') as jsonfile:
                json_com = json.load(jsonfile)
                for entry in json_com:
                    import ipdb; ipdb.set_trace()
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

                self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"'))
