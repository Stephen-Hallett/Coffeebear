from django.db import models
from django.urls import reverse

class Cafe(models.Model):
    name = models.CharField(max_length=20, unique=True)
    sans_coffee_rating = models.FloatField()
    stephen_coffee_rating = models.FloatField()
    food_rating = models.FloatField(blank=True, null=True)
    ambience_rating = models.FloatField(blank=True, null=True)
    review = models.TextField(help_text="Cafe Review", blank=True, null=True)
    latitude = models.DecimalField(max_digits=25,decimal_places=21, blank=True, null=True)
    longitude = models.DecimalField(max_digits=25,decimal_places=21, blank=True, null=True)
    main_image = models.ImageField(upload_to="map/static/map/main_images",blank=True, null=True)
    sub_images = models.ImageField(upload_to="map/static/map/sub_images", blank=True, null=True)
    address = models.CharField(max_length=100)

    @property
    def coffee_rating(self):
        coffee_rating = round((self.sans_coffee_rating + self.stephen_coffee_rating)/2, 2)
        return coffee_rating

    @property
    def overall_rating(self):
        if self.ambience_rating and self.food_rating:
            overall_rating = (self.coffee_rating + self.food_rating + self.ambience_rating)/3
        elif self.ambience_rating:
            overall_rating = (self.coffee_rating + self.ambience_rating)/2
        elif self.food_rating:
            overall_rating = (self.coffee_rating + self.food_rating)/2
        else:
            overall_rating = self.coffee_rating
        return round(overall_rating,2)
        

    def __str__(self):
        return self.name

class Suburb(models.Model):
    name = models.CharField(max_length=20)
    cafes = models.ManyToManyField(Cafe,blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=20)
    suburbs = models.ManyToManyField(Suburb,blank=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=20)
    cities = models.ManyToManyField(City,blank=True)

    def __str__(self):
        return self.name
