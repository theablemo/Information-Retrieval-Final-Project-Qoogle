import requests
from django.db import models
from model_utils.models import TimeStampedModel

from information_retrieval.enums import Engine
from information_retrieval.lib.boolean_engine import BooleanEngine
from information_retrieval.lib.surah_metadata import surah_metas
from information_retrieval.lib.tfidf_engine import TFIDFEngine
from information_retrieval.lib.fasttext_engine import FastTextEngine
from information_retrieval.lib.transformer_engine import TransformerEngine


class Query(TimeStampedModel):
    text = models.CharField(max_length=511)
    engine = models.PositiveSmallIntegerField(default=0, choices=Engine.choices)
    responses = models.ManyToManyField(to='Response')

    engines = {
        Engine.BOOLEAN: BooleanEngine,
        Engine.TFIDF: TFIDFEngine,
        Engine.FASTTEXT: FastTextEngine,
        Engine.TRANSFORMER: TransformerEngine,
    }

    def __str__(self):
        return f"{self.text} @ {Engine(self.engine).name}"

    def process(self):
        assert self.engine in Query.engines.keys(), "Engine not found."
        raw_responses = Query.engines[Engine(self.engine)].process_query(self.text)
        for raw_response in raw_responses:
            verse_number = raw_response['verse_number']
            surah_number = raw_response['surah_number']
            surah_name = Response.retrieve_surah_name(surah_number=surah_number)
            verse = complete_verse = raw_response['verse']
            # api_response = requests.get(f"https://api.alquran.cloud/v1/ayah/{surah_number}:{verse_number}")
            # if api_response.status_code == 200:
            #     complete_verse = api_response.json()['data']['text']
            response, _ = Response.objects.update_or_create(verse=verse,
                                                         verse_number=verse_number,
                                                         surah_name=surah_name,
                                                         surah_number=surah_number,
                                                         complete_verse=complete_verse)
            self.responses.add(response)


class Response(TimeStampedModel):
    verse = models.CharField(max_length=511)
    complete_verse = models.TextField(null=True, default="")
    verse_number = models.CharField(max_length=511)
    surah_number = models.IntegerField(default=2)
    surah_name = models.CharField(max_length=127, null=True)

    @staticmethod
    def retrieve_surah_name(surah_number):
        for surah in surah_metas:
            if surah['number'] == surah_number:
                return surah['name']
        return None

    def __str__(self):
        return f"{self.verse}"

