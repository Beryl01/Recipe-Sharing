from django.http import HttpResponse, Http404
from .models import Profile, Recipe, RecipeIngredient
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, UpdateProfileForm, postRecipeForm, UpdateRecipeForm, Registration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'auth/registration.html',{"form":form})

def index(request):
    recipe = Recipe.objects.all()
    return render(request, 'index.html',{"recipe":recipe})

@login_required
def profile(request,id): 
    try: 
        current_user = request.user
        profile = Profile.objects.filter(user_id=id).all()
        recipe = Recipe.objects.filter(user=current_user.profile).all()
        return render(request, 'profile.html', {"profile":profile,"recipe":recipe}) 
    except User.profile.RelatedObjectDoesNotExist:
        return redirect(update_profile)

@login_required
def update_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')
    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html',{"form":form})

@login_required
def deleteaccount(request):
    current_user = request.user
    account = User.objects.get(pk=current_user.id)
    account.delete()
    return redirect('register')

@login_required
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = postImageForm(request.POST,request.FILES) 
        if form.is_valid():
            post = form.save(commit = False)
            post.profile = current_user.profile
            post.save()
            return redirect('index')
    else:
        form = postImageForm()
    return render(request, 'post.html',{"form":form})  

@login_required
def update_recipe(request):
    current_user = request.user
    if request.method=="POST":
        form = UpdateRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            updatepost = form.save(commit=False)
            updatepost.profile = current_user.profile
            updatepost.save()
            messages.success(request,'Your Recipe has been updated successfully')
            return redirect('index')
    else:
        form = UpdateRecipeForm()
    return render(request, 'updaterecipe.html',{"form":form})                     

@login_required
def delete(request,image_id):
    image = Image.objects.get(pk=image_id)
    if image:
        image.delete_image()
    return redirect('profile')

@login_required
def delete(request,image_id):
    image = Image.objects.get(pk=image_id)
    image.delete()
    return redirect('profile')    

def all(request):
    recipe = Recipe.objects.all()
    return render(request, 'all.html',{"recipe":recipe})

def country(request):
    image = Image.objects.all()
    countries = Country.objects.all()
    return render(request, 'country.html', {"image": image, "countries": countries})    

def search_by_country(request, country):
    countries = Country.objects.all()
    image = Image.search_by_country(country)
    return render(request, 'country.html', {"image": image, "countries": countries}) 

def ingredient(request):
    image = Image.objects.all()
    recipeingredients = RecipeIngredient.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient.html', {"image": image, "ingredients": ingredients, "recipeingredients": recipeingredients}) 

def search_by_ingredient(request, ingredient):
    ingredients = Ingredient.objects.all()
    # recipeingredients = RecipeIngredient.objects.all()
    image = Image.search_by_ingredient(ingredient)
    return render(request, 'ingredient.html', {"image": image, "ingredients": ingredients})           
