from ast import Add
from django.contrib import admin
from .models import Cafe, Suburb, City, Country


class CafeAdmin(admin.ModelAdmin):
    list_display = ("name","overall_rating","coffee_rating", "food_rating", "ambience_rating")

class SuburbAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Cafe, CafeAdmin)
admin.site.register(Suburb, SuburbAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)