from django.http import HttpResponse, Http404
from .models import Profile, Recipe, RecipeIngredient, Country
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
    return render(request, 'index.html')

def recipes(request):
    recipe = Recipe.objects.all()
    return render(request, 'recipes.html',{"recipe":recipe})    

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
            return redirect('recipes')
    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html',{"form":form})

@login_required
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = postRecipeForm(request.POST,request.FILES) 
        if form.is_valid():
            post = form.save(commit = False)
            post.profile = current_user.profile
            post.save()
            return redirect('recipes')
    else:
        form = postRecipeForm()
    return render(request, 'post.html',{"form":form})  

@login_required
def update_recipe(request):
    current_user = request.user
    if request.method=="POST":
        form = UpdateRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            update_recipe = form.save(commit=False)
            profile.user = current_user
            update_recipe.save()
            messages.success(request,'Your Recipe has been updated successfully')
            return redirect('recipes')
    else:
        form = UpdateRecipeForm()
    return render(request, 'updaterecipe.html',{"form":form}) 

@login_required
def single(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    current_user = request.user
    return render(request,'single.html',{"recipe":recipe})

def all(request):
    recipe = Recipe.objects.all()
    return render(request, 'all.html',{"recipe":recipe})
    
@login_required
def country(request):
    recipe = Recipe.objects.all()
    countries = Country.objects.all()
    return render(request, 'country.html', {"recipe":recipe, "countries": countries})    

@login_required
def search_by_country(request, country):
    countries = Country.objects.all()
    recipe = Recipe.search_by_country(country)
    return render(request, 'country.html', {"recipe":recipe, "countries": countries}) 

@login_required
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_recipe = Recipe.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"recipe": searched_recipe})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

