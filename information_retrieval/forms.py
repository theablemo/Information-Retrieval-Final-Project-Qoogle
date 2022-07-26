from django import forms

from information_retrieval.models import Query


class QueryForm(forms.ModelForm):
    text = forms.CharField()
    engine = forms.IntegerField()

    class Meta:
        model = Query
        fields = ['text', 'engine']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        engine = cleaned_data.get('engine')
        if engine:
            if not 0 <= engine <= 4:
                self.add_error('engine', 'Engine should be in [0, 3] range.')
