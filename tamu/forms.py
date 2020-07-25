from django import forms
from .models import Profile, Recipe, RecipeIngredient, Country
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class Registration(UserCreationForm):
    '''
    class to define registration form
    '''
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['user']
        fields = ('bio', 'profile_pic','contacts')

class UpdateProfileForm(forms.ModelForm):
    '''
    class to define updateprofile form
    '''
    class Meta:
        model = Profile
        fields = ['profile_pic','bio', 'contacts']                

class postrecipeingredientForm(forms.ModelForm):
    '''
    class to define posted recipe form
    '''
    class Meta:
        model = RecipeIngredient
        fields = ['name']         

class postRecipeForm(forms.ModelForm):
    '''
    class to define posted recipe form
    '''
    class Meta:
        model = Recipe
        fields = ['image', 'name', 'recipe', 'ingredient', 'country', 'people_served']    

class UpdateRecipeForm(forms.ModelForm):
    '''
    class to define updaterecipe form
    '''
    class Meta:
        model = Recipe
        fields = ['image', 'name', 'recipe', 'ingredient', 'country' , 'people_served']           



