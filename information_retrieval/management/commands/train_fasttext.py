from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from information_retrieval.lib.quran_mir.quran_ir import FasttextQuranIR
        FasttextQuranIR.train(create_dataset=True)
