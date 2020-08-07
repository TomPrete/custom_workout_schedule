from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_app, name='main_app'),
    path('programs', views.all_programs, name='all_programs'),
    path('workouts', views.all_workouts, name='all_workouts'),
    path('categories', views.all_categories, name='all_categories'),
    path('workout/<int:workout_id>', views.workout_detail, name='workout_detail'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('products', views.affiliate_page, name='affiliate_page'),
    path('about', views.about, name='about'),
    path('download-csv', views.download_workout_csv, name='download_workout_csv'),
]
