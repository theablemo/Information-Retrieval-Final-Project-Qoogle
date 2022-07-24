class BaseEngine:

    @staticmethod
    def process_query(text):
        """
        This function is for searching a text query in quran by any implemented models
        :param text: the query text to search in Quran
        :return: list of dictionaries with this format:
        [
            {
                "verse": "الم",
                "verse_number": 1,
                "surah_name": "بقره",
            }, ...
        ]
        """
        raise NotImplementedError
