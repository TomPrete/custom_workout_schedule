from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_app, name='main_app'),
    path('programs', views.all_programs, name='all_programs'),
    path('workouts', views.all_workouts, name='all_workouts'),
    path('workout/<str:workout_id>', views.workout_detail, name='workout_detail'),
    path('products', views.affiliate_page, name='affiliate_page'),
]
