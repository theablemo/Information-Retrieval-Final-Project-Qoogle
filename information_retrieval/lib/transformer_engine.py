from information_retrieval.lib.base_engine import BaseEngine

from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer, quran_series
from information_retrieval.lib.quran_mir.tools import get_most_similars
from information_retrieval.lib.quran_mir.transformer_retrieval import sent_to_vec, merged_corpus_embeddings


class TransformerEngine(BaseEngine):

    @staticmethod
    def process_query(text):
        query_vec = sent_to_vec(quran_normalizer(text))
        results = list(get_most_similars(quran_series, merged_corpus_embeddings,
                                         query_vec, 10, check_moghattaeh=True).to_dict('records'))
        return [
            {
                "verse": result,
                "verse_number": 1,
                "surah_name": "Baghareh",
            } for result in results
        ]
