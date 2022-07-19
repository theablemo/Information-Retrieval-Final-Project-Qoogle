from django.db import models
from model_utils.models import TimeStampedModel


class Query(TimeStampedModel):
    text = models.CharField(max_length=511)
    engine = models.PositiveSmallIntegerField(default=0)


class Response(TimeStampedModel):
    verse = models.CharField(max_length=511)
    verse_number = models.CharField(max_length=511)
    surah_name = models.CharField(max_length=127)

