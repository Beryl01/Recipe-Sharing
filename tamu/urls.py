from django.urls import path,re_path
from . import views as views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
    re_path(r'^profile/(\d+)',views.profile,name = 'profile'),
    path('update/',views.update_profile,name='update_profile'),
    re_path(r'^deleteaccount/$',views.deleteaccount,name='deleteaccount'),
    path('post/',views.post,name='post'),
    path('updaterecipe/',views.update_recipe,name='update_recipe'),
    re_path(r'^delete/(?P<image>\d+)$',views.delete,name='delete'),
    path('all/', views.all, name='all'),
    path('country/', views.country, name='country'),
    re_path(r'^country/(?P<country>\d+)',views.search_by_country, name='country_filter'),
    path('ingredient/', views.ingredient, name='ingredient'),
    re_path(r'^ingredient/(?P<ingredient>\d+)',views.search_by_ingredient, name='ingredient_filter'),
]