from django.db import models
from model_utils.models import TimeStampedModel

from information_retrieval.enums import Engine
from information_retrieval.lib.boolean_engine import BooleanEngine
from information_retrieval.lib.tfidf_engine import TFIDFEngine
# from information_retrieval.lib.fasttext_engine import FastTextEngine
# from information_retrieval.lib.transformer_engine import TransformerEngine


class Query(TimeStampedModel):
    text = models.CharField(max_length=511)
    engine = models.PositiveSmallIntegerField(default=0, choices=Engine.choices)
    responses = models.ManyToManyField(to='Response')

    engines = {
        Engine.BOOLEAN: BooleanEngine,
        Engine.TFIDF: TFIDFEngine,
        # Engine.FASTTEXT: FastTextEngine,
        # Engine.TRANSFORMER: TransformerEngine,
    }

    def __str__(self):
        return f"{self.text} @ {Engine(self.engine).name}"

    def process(self):
        assert self.engine in Query.engines.keys(), "Engine not found."
        raw_responses = Query.engines[Engine(self.engine)].process_query(self.text)
        for raw_response in raw_responses:
            response, _ = Response.objects.get_or_create(verse=raw_response['verse'],
                                                         verse_number=raw_response['verse_number'],
                                                         surah_name=raw_response['surah_name'])
            self.responses.add(response)


class Response(TimeStampedModel):
    verse = models.CharField(max_length=511)
    verse_number = models.CharField(max_length=511)
    surah_name = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.verse}"

