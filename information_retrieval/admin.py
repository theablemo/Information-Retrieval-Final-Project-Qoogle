from django.contrib.admin import register, ModelAdmin

from information_retrieval.models import Query


@register(Query)
class QueryAdmin(ModelAdmin):
    list_display = ['text', 'engine']
