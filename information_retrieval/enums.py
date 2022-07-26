from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _


class Engine(models.IntegerChoices):
    BOOLEAN = 0, _('Boolean Model')
    TFIDF = 1, _('TF-IDF Model')
    FASTTEXT = 2, _('Fast Text Model')
    TRANSFORMER = 3, _('Transformer Model'),
    ELASTIC = 4, _('Elastic Search Model')
