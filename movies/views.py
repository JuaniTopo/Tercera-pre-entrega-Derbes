from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from movies.forms import MovieForm, CountryForm, DirectorForm, ProductionCompanyForm, SearchForm
from movies.models import Movie, Country, Director, ProductionCompany

class MovieFormView(FormView):
    template_name = 'movie.html'
    form_class = MovieForm
    success_url = '/movies/thanks/'

    def form_valid(self, form):
        movie = Movie()
        movie.name = form.cleaned_data['name']
        movie.genre = form.cleaned_data['genre']
        movie.production_company = form.cleaned_data['production_company']
        movie.score = form.cleaned_data['score']
        movie.age_restricted = form.cleaned_data['age_restricted']
        movie.save()
        return super(MovieFormView, self).form_valid(form)

class DirectorFormView(FormView):
    template_name = 'director.html'
    form_class = DirectorForm
    model = Director
    success_url ='/movies/thanks/'

    def form_valid(self, form):
        director = Director()
        director.name = form.cleaned_data['name']
        director.surname = form.cleaned_data['surname']
        director.birthday = form.cleaned_data['birthday']
        director.country = form.cleaned_data['country']
        director.save()
        return super(DirectorFormView, self).form_valid(form)

class CountryFormView(FormView):
    template_name = 'country.html'
    form_class = CountryForm
    success_url = '/movies/thanks/'

    def form_valid(self, form):
        country = Country()
        country.name = form.cleaned_data['name']
        country.foundation_date = form.cleaned_data['foundation_date']
        country.continent = form.cleaned_data['continent']
        country.save()
        return super(CountryFormView, self).form_valid(form)


class ProductionCompanyFormView(FormView):
    template_name = 'productioncompany.html'
    form_class = ProductionCompanyForm
    success_url = '/movies/thanks/'

    def form_valid(self, form):
        production_company = ProductionCompany()
        production_company.name = form.cleaned_data['name']
        production_company.country_of_origin = form.cleaned_data['country_of_origin']
        production_company.foundation_date = form.cleaned_data['foundation_date']
        production_company.save()
        return super(ProductionCompanyFormView, self).form_valid(form)

def search(request):
    search_form = SearchForm(request.POST or None)
    if request.POST:
        if search_form.is_valid():
            if request.POST['type_of_search'] == 'movie':
                results = Movie.objects.filter(title__icontains=request.POST['name'])
            elif request.POST['type_of_search'] == 'country':
                results = Country.objects.filter(name__icontains=request.POST['name'])
            elif request.POST['type_of_search'] == 'director':
                results = Director.objects.filter(name__icontains=request.POST['name'])
            elif request.POST['type_of_search'] == 'productioncompany':
                results = ProductionCompany.objects.filter(name__icontains=request.POST['name'])
            return render(request, 'results.html', {'results': results, 'type': request.POST['type_of_search']})
    else:
        return render(request, 'search.html', {'search_form': search_form})

class ThanksPageView(TemplateView):
    template_name = 'thanks.html'