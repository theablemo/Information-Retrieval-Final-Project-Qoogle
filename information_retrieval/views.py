from django.shortcuts import render

from information_retrieval.lib.quran_mir.Query_expansion import QueryExpansion
from information_retrieval.lib.quran_mir.quran_ranker import QuranRanker
from information_retrieval.lib.fasttext_engine import FastTextEngine
from information_retrieval.models import Query, Response
from qoogle.settings import BASE_URL

query_expansion = QueryExpansion()
quran_ranker = QuranRanker(FastTextEngine.get_ir_model())


def search_query(request):
    return render(request, 'search_bar.html')


def search_results(request):
    text = request.GET['text']
    engine = int(request.GET['engine'])
    query, _ = Query.objects.get_or_create(text=text, engine=engine)
    query.process()
    results = list(query.responses.order_by('rank'))
    # cluster = None  # TODO: retrieve cluster
    # classification_1 = None  # TODO: retrieve classification type 1
    # classification_2 = None  # TODO: retrieve classification type 2
    expanded_query = query_expansion.expand_query(text)

    return render(request, 'search_results.html', {
        'text': text,
        'results': results,
        'base_url': BASE_URL,
        'engine': str(engine),
        'expanded_query': expanded_query,
    })


def lucky_query(request):
    return render(request, 'lucky_bar.html', {
        'all_sureh': {i: Response.retrieve_surah_name(i) for i in range(1, 115)}
    })


def lucky_results(request):
    text = '!محور سوره مبارکه را بیاب'
    surah_index = int(request.GET['engine'])
    sureh_name = Response.retrieve_surah_name(surah_index)
    verse_text, verse_num = quran_ranker.get_pivot_aye(sureh_name)

    return render(request, 'lucky_results.html', {
        'text': text,
        'sureh_index': surah_index,
        'engine': str(surah_index),
        'base_url': BASE_URL,
        'verse_text': verse_text,
        'verse_num': verse_num,
    })
