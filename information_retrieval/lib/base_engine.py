class BaseEngine:

    @staticmethod
    def dataframe_to_dict(df):
        df = df.reset_index()
        raw_results = df.T.to_dict().values()
        results = []
        for result in raw_results:
            surah_number, verse_number = result[df.columns[0]].split("##")
            results.append({
                "verse": result['آیه'],
                "verse_number": int(verse_number),
                "surah_number": int(surah_number),
            })
        return results

    @staticmethod
    def process_query(text, k=10):
        """
        This function is for searching a text query in quran by any implemented models
        :param text: the query text to search in Quran
        :param K: count of search results to return
        :return: list of dictionaries with this format:
        [
            {
                "verse": "الم",
                "verse_number": 1,
                "surah_number": 2,
            }, ...
        ]
        """
        raise NotImplementedError
