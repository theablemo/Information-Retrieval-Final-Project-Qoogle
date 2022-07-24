from django.db import models
from model_utils.models import TimeStampedModel

from information_retrieval.enums import Engine


class Query(TimeStampedModel):
    text = models.CharField(max_length=511)
    engine = models.PositiveSmallIntegerField(default=0, choices=Engine.choices)
    responses = models.ManyToManyField(to='Response')

    engines = {
        Engine.BOOLEAN: None,
        Engine.TFIDF: None,
        Engine.FASTTEXT: None,
        Engine.TRANSFORMER: None,
    }

    def __str__(self):
        return f"{self.text} @ {Engine(self.engine).name}"

    def process(self):
        assert self.engine in Query.engines.keys(), "Engine not found."
        raw_responses = Query.engines[Engine(self.engine)].process_query(self.text)
        for raw_response in raw_responses:
            response = Response.objects.get_or_create(verse=raw_response)
            self.responses.add(response)


class Response(TimeStampedModel):
    verse = models.CharField(max_length=511)
    verse_number = models.CharField(max_length=511)
    surah_name = models.CharField(max_length=127)

