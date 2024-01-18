from django import forms
from scraping.models import City, Language
class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), label='Город',
        to_field_name='slug', required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), required=False,
        to_field_name='slug', label='Специальность',
        widget=forms.Select(attrs={'class': 'form-control'}))