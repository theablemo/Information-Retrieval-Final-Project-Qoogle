from django.shortcuts import render

from information_retrieval.forms import QueryForm
from information_retrieval.models import Query
from qoogle.settings import BASE_URL


def search_query(request):
    return render(request, 'search_bar.html')


def search_results(request):
    text = request.GET['text']
    engine = int(request.GET['engine'])
    query, _ = Query.objects.get_or_create(text=text, engine=engine)
    query.process()
    results = list(query.responses.all())
    cluster = None  # TODO: retrieve cluster
    classification_1 = None  # TODO: retrieve classification type 1
    classification_2 = None  # TODO: retrieve classification type 2

    return render(request, 'search_results.html', {'text': text,
                                                   'results': results,
                                                   'base_url': BASE_URL,
                                                   'engine': str(engine),
                                                   'cluster': cluster,
                                                   'classification_1': classification_1,
                                                   'classification_2': classification_2,
                                                   })
