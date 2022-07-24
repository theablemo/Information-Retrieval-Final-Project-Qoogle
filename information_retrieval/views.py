from django.shortcuts import render

from information_retrieval.forms import QueryForm
from information_retrieval.models import Query


def search_query(request):
    return render(request, 'search_bar.html')


def search_results(request):
    text = request.GET['text']
    engine = 0  # TODO: read engine from template
    query, _ = Query.objects.get_or_create(text=text, engine=engine)
    print(query)
    query.process()
    results = query.responses

    return render(request, 'search_results.html', {'text': text,
                                                   'results': results})
