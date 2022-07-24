from django.shortcuts import render

from information_retrieval.forms import QueryForm
from information_retrieval.models import Query
from qoogle.settings import BASE_URL


def search_query(request):
    return render(request, 'search_bar.html')


def search_results(request):
    text = request.GET['text']
    engine = 2  # TODO: read engine from template
    query, _ = Query.objects.get_or_create(text=text, engine=engine)
    query.process()
    results = list(query.responses.all())

    return render(request, 'search_results.html', {'text': text,
                                                   'results': results,
                                                   'base_url': BASE_URL})
