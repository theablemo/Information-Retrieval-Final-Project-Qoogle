from django.core.management import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import elasticsearch
import pandas as pd

SETTINGS = {
    "settings": {
        "analysis": {
            "filter": {
                "arabic_stop": {
                    "type":       "stop",
                    "stopwords":  "_arabic_"
                },
                "arabic_keywords": {
                    "type":       "keyword_marker",
                    "keywords":   ["مثال"]
                },
                "arabic_stemmer": {
                    "type":       "stemmer",
                    "language":   "arabic"
                }
            },
            "analyzer": {
                "rebuilt_arabic": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "decimal_digit",
                        "arabic_stop",
                        "arabic_normalization",
                        # "arabic_keywords",
                        # "arabic_stemmer"
                    ]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "text": {
                "type": "text",
                "analyzer": "arabic"
            }
        }
    }
}


def generator(df):
    for c, line in enumerate(df):
        yield{
            '_index': 'quran',

            '_id': c,
            '_source': {
                'chapter': line.get('chapter', None),
                'verse': line.get('verse', None),
                'text': line.get('text', None),
            }
        }


class Command(BaseCommand):
    def handle(self, *args, **options):
        es = Elasticsearch("http://localhost:9200")
        quran_path = 'information_retrieval/lib/quran_mir/data/quran-simple.txt'
        quran_df = pd.read_csv(quran_path, sep='|')
        json_from_df = quran_df.to_dict('records')
        es.indices.create(index='quran', ignore=[400, 404], body=SETTINGS)
        try:
            res = helpers.bulk(es, generator(json_from_df))
        except Exception as e:
            pass
