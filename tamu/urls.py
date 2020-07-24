from django.urls import path,re_path
from . import views as views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('recipes',views.recipes,name='recipes'),
    path('register',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
    re_path(r'^profile/(\d+)',views.profile,name = 'profile'),
    path('update/',views.update_profile,name='update_profile'),
    path('post/',views.post,name='post'),
    re_path(r'^recipe/(\d+)',views.single,name='recipe'),
    path('updaterecipe/',views.update_recipe,name='update_recipe'),
    path('all/', views.all, name='all'),
    path('country/', views.country, name='country'),
    re_path(r'^country/(?P<country>\d+)',views.search_by_country, name='country_filter'),
    # re_path(r'^search/',views.search_results, name='search_results'),
]