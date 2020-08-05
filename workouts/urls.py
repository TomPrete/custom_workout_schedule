from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_app, name='main_app'),
    path('programs', views.all_programs, name='all_programs'),
    path('workouts', views.all_workouts, name='all_workouts'),
    path('workout/<int:workout_id>', views.workout_detail, name='workout_detail'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('products', views.affiliate_page, name='affiliate_page'),
    path('download-csv/<str:schedule>', views.save_workout_to_csv, name='save_workout_to_csv'),
]
