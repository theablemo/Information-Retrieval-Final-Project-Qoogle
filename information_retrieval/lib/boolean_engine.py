from information_retrieval.lib.base_engine import BaseEngine
from information_retrieval.lib.quran_mir.boolean_retrieval.ir_system import IRSystem
from information_retrieval.lib.quran_mir.preprocess_quran_text import verse_complete_dict


class BooleanEngine(BaseEngine):

    @staticmethod
    def process_query(text):
        docs_complete = [*verse_complete_dict.values()]
        boolean_ir_complete = IRSystem(docs_complete)
        results = boolean_ir_complete.process_query(text, "complete")
        return [
            {
                "verse": result,
                "verse_number": 1,
                "surah_name": "Baghareh",
            } for result in results
        ]
