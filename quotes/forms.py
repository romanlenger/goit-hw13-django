from django import forms

from .models import Quote, Author


class QuoteForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Виберіть автора", required=True)

    class Meta:
        model = Quote
        fields = ['author', 'quote', 'tags']
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введіть текст цитати'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Введіть теги через кому'}),
        }

