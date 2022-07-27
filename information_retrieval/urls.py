from django.urls import path

from information_retrieval import views

urlpatterns = [
    path('', views.search_query, name="search_query"),
    path('lucky/', views.lucky_query, name="lucky_query"),
    path('search/', views.search_results, name="search_results"),
    path('lucky/search', views.lucky_results, name="lucky_results"),
]
