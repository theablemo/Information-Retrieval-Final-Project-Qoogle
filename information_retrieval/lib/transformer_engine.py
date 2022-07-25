from information_retrieval.lib.base_engine import BaseEngine

from information_retrieval.lib.quran_mir.preprocess_quran_text import quran_normalizer
from information_retrieval.lib.quran_mir.quran_ir import ArabertQuranIR


class TransformerEngine(BaseEngine):

    @staticmethod
    def process_query(text, k=10):
        arabert_quran_ir = ArabertQuranIR()
        results_df = arabert_quran_ir.get_most_similars(quran_normalizer(text), K=k)
        return BaseEngine.dataframe_to_dict(results_df)
