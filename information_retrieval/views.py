from django.shortcuts import render

from information_retrieval.lib.quran_mir.Query_expansion import QueryExpansion
from information_retrieval.models import Query
from qoogle.settings import BASE_URL

query_expansion = QueryExpansion()


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
        # 'cluster': cluster,
        # 'classification_1': classification_1,
        # 'classification_2': classification_2,
        'expanded_query': expanded_query,
    })


def lucky_query(request):
    return render(request, 'lucky_bar.html')


def lucky_results(request):
    text = request.GET['text']
    engine = int(request.GET['engine'])
    query, _ = Query.objects.get_or_create(text=text, engine=engine)
    query.process()
    results = list(query.responses.order_by('rank'))
    # cluster = None  # TODO: retrieve cluster
    # classification_1 = None  # TODO: retrieve classification type 1
    # classification_2 = None  # TODO: retrieve classification type 2
    expanded_query = query_expansion.expand_query(text)

    return render(request, 'lucky_results.html', {
        'text': text,
        'results': results,
        'base_url': BASE_URL,
        'engine': str(engine),
        # 'cluster': cluster,
        # 'classification_1': classification_1,
        # 'classification_2': classification_2,
        'expanded_query': expanded_query,
    })
