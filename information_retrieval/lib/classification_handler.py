import pandas as pd



class ClassificationHandler:

    def get_surah_predication_v1(self, surah_number, verse_number):
        df = pd.read_csv('information_retrieval/lib/classification_data/classification-fasttext.csv')
        try:
            surah_number = \
            df[(df['شماره سوره'] == surah_number) & (df['شماره آیه'] == verse_number)]['predicted_sure'].values[0]
            from information_retrieval.models import Response
            return Response.retrieve_surah_name(surah_number=surah_number)
        except IndexError:
            return None


    def get_surah_predication_v2(self, surah_number, verse_number):
        try:
            df = pd.read_csv('information_retrieval/lib/classification_data/classification-bert.csv')
            surah_number = df[(df['شماره سوره'] == surah_number) & (df['شماره آیه'] == verse_number)]['predicted_sure'].values[0]
            from information_retrieval.models import Response
            return Response.retrieve_surah_name(surah_number=surah_number)
        except IndexError:
            return None

    def get_makki_madani_predication(self, surah_number):
        df = pd.read_csv('information_retrieval/lib/classification_data/clustering-makki-madani-top-performance.csv')
        return df[df['شماره سوره'] == surah_number]['predicted'].values[0]

    def get_makki_madani_real(self, surah_number):
        df = pd.read_csv('information_retrieval/lib/classification_data/clustering-makki-madani-top-performance.csv')
        return df[df['شماره سوره'] == surah_number]['نوع سوره'].values[0]

    def get_four_cluster_type(self, surah_number):
        df = pd.read_csv('information_retrieval/lib/classification_data/clustering-4clusters.csv')
        return int(df[df['شماره سوره'] == surah_number]['cluster'].values[0]) + 1

