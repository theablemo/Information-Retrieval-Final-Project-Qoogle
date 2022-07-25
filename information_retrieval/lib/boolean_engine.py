from information_retrieval.lib.base_engine import BaseEngine
from information_retrieval.lib.quran_mir.boolean_retrieval.ir_system import IRSystem
from information_retrieval.lib.quran_mir.preprocess_quran_text import verse_complete_dict
from information_retrieval.lib.quran_mir.quran_ir import BooleanQuranIR


class BooleanEngine(BaseEngine):

    @staticmethod
    def process_query(text, k=10):
        boolean_quran_ir = BooleanQuranIR()
        results_df = boolean_quran_ir.get_most_similars(text, K=k)
        return BaseEngine.dataframe_to_dict(results_df)
