from information_retrieval.lib.base_engine import BaseEngine

from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer
from information_retrieval.lib.quran_mir.quran_ir import ArabertQuranIR
from qoogle.settings import import_config

from elasticsearch import Elasticsearch

class ElasticEngine(BaseEngine):
    ir_model = None

    @staticmethod
    def get_ir_model():
        if TransformerEngine.ir_model is None:
            TransformerEngine.ir_model = ArabertQuranIR()
        return TransformerEngine.ir_model

    @staticmethod
    def process_query(text, k=10):
        # arabert_quran_ir = TransformerEngine.get_ir_model()
        # results_df = arabert_quran_ir.get_most_similars(quran_normalizer(text), K=k)
        # return BaseEngine.dataframe_to_dict(results_df)
        # elastic_ip = import_config(name="ELASTIC_IP")
        es = Elasticsearch("http://localhost:9200")
        res = es.search(index="quran",source=['chapter', 'verse', 'text'], size=k, query = {"match": {"text": text}})["hits"]["hits"]
        a = []
        for i in res:
            a.append({
                "verse": i["_source"]["text"],
                "verse_number": i["_source"]["verse"],
                "surah_number": i["_source"]["chapter"],
            })
        return a