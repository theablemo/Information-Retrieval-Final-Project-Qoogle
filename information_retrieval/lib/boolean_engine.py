from information_retrieval.lib.base_engine import BaseEngine
from information_retrieval.lib.quran_mir.boolean_retrieval.ir_system import IRSystem
from information_retrieval.lib.quran_mir.preprocess_quran_text import verse_complete_dict
from information_retrieval.lib.quran_mir.quran_ir import BooleanQuranIR


class BooleanEngine(BaseEngine):
    ir_model = None

    @staticmethod
    def get_ir_model():
        if BooleanEngine.ir_model is None:
            BooleanEngine.ir_model = 1
            BooleanEngine.ir_model = BooleanQuranIR()
        return BooleanEngine.ir_model

    @staticmethod
    def process_query(text, k=10):
        boolean_quran_ir = BooleanEngine.get_ir_model()
        results_df = boolean_quran_ir.get_most_similars(text, K=k)
        return BaseEngine.dataframe_to_dict(results_df)
