from django.urls import path

from information_retrieval import views

urlpatterns = [
    path('', views.search_query, name="search_query"),
    path('search/', views.search_results, name="search_results"),
]
