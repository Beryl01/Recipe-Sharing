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

class Recipe(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=70)
    ingredient = models.ManyToManyField(RecipeIngredient)
    recipe = models.TextField()
    people_served = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    image = CloudinaryField('image')
    posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name     
