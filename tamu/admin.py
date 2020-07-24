from django.contrib import admin
from .models import Profile, Recipe, RecipeIngredient, Country

# Register your models here.
admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Country)
admin.site.register(RecipeIngredient)