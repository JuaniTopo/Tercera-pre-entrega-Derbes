from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    director = models.ForeignKey('Director', on_delete=models.PROTECT)
    score = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    production_company = models.ForeignKey('ProductionCompany', null=True, on_delete=models.PROTECT)
    age_restricted = models.BooleanField(null=True)

class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    country = models.ForeignKey('Country', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Country(models.Model):
    name = models.CharField(max_length=20)
    foundation_date = models.DateField(null=True)
    continent = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "{}".format(self.name)

class ProductionCompany(models.Model):
    name = models.CharField(max_length=40)
    country_of_origin = models.ForeignKey('Country', on_delete=models.PROTECT)
    foundation_date = models.DateField(null=True)

    def __str__(self):
        return "{}".format(self.name)

