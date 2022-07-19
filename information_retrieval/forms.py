from django import forms


class QueryForm(forms.ModelForm):
    text = forms.CharField()
    engine = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        engine = cleaned_data.get('engine')
        # if email:
        #     if User.objects.filter(email=email).exists():
        #         self.add_error('email', 'This email is already in use')