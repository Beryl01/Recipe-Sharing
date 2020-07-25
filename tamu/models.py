from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt
from django_countries.fields import CountryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('profile_pic')
    bio = models.CharField(max_length = 100)
    contacts = models.CharField(max_length = 100)

    def __str__(self):
        return self.bio

class RecipeIngredient(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name 

class Country(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place         

class Recipe(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=70)
    ingredient = models.ManyToManyField(RecipeIngredient)
    recipe = models.TextField()
    people_served = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name   

    @classmethod
    def get_recipe_by_id(cls,recipe_id):
        recipe = cls.objects.get(id=recipe_id)
        return recipe

    @classmethod
    def search_by_country(cls, search_term):
        recipe = Recipe.objects.filter(country__id=search_term).all()
        return recipe     

