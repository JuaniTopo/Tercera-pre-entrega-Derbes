from django import forms
from movies.models import Director, Country, ProductionCompany

class MovieForm(forms.Form):
    title = forms.CharField(max_length=50)
    genre = forms.CharField(max_length=20)
    director = forms.ModelChoiceField(queryset=Director.objects.all())
    score = forms.DecimalField(decimal_places=2, max_digits=3, required=False)
    production_company = forms.ModelChoiceField(queryset=ProductionCompany.objects.all(), required=False)
    age_restricted = forms.BooleanField(required=False)

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1850,2020)),required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False)

class CountryForm(forms.Form):
    name = forms.CharField(max_length=20)
    foundation_date = forms.DateField(required=False)
    continent = forms.CharField(max_length=20, required=False)

class ProductionCompanyForm(forms.Form):
    name = forms.CharField(max_length=40)
    country_of_origin = forms.ModelChoiceField(queryset=Country.objects.all())
    foundation_date = forms.DateField(required=False)

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)
    type_of_search = forms.CharField(max_length=100)