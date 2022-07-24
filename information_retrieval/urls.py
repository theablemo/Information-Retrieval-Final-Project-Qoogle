from django.urls import path

from information_retrieval import views

urlpatterns = [
    path('', views.search_query, name="search_query"),
]
