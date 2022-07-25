from information_retrieval.lib.base_engine import BaseEngine

from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer
from information_retrieval.lib.quran_mir.quran_ir import FasttextQuranIR


class FastTextEngine(BaseEngine):

    @staticmethod
    def process_query(text, k=10):
        fasttext_quran_ir = FasttextQuranIR()
        results_df = fasttext_quran_ir.get_most_similars(quran_normalizer(text), K=k)
        return BaseEngine.dataframe_to_dict(results_df)
