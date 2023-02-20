from django.contrib import admin
from django.urls import path
from movies.views import MovieFormView, DirectorFormView, CountryFormView, ProductionCompanyFormView, search, ThanksPageView

urlpatterns = [
    path('movie/', MovieFormView.as_view(), name='movie'),
    path('director/', DirectorFormView.as_view(), name='director'),
    path('country/', CountryFormView.as_view(), name='country'),
    path('productioncompany/', ProductionCompanyFormView.as_view(), name='productioncompany'),
    path('search/', search, name='search'),
    path('thanks/', ThanksPageView.as_view(), name='thanks'),
]