from django.contrib.admin import register, ModelAdmin

from information_retrieval.models import Query, Response


@register(Response)
class QueryAdmin(ModelAdmin):
    list_display = ['verse', 'verse_number', 'surah_name']


@register(Query)
class QueryAdmin(ModelAdmin):
    list_display = ['text', 'engine']
