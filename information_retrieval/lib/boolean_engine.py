from information_retrieval.lib.ir_package import BaseEngine
from information_retrieval.lib.quran_mir.boolean_retrieval.ir_system import IRSystem
from information_retrieval.lib.quran_mir.preprocess_quran_text import verse_complete_dict


class BooleanEngine(BaseEngine):
    def process_query(self, text):
        docs_complete = [*verse_complete_dict.values()]
        boolean_ir_complete = IRSystem(docs_complete)
        result = boolean_ir_complete.process_query(text, "complete")
        return result
