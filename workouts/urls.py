from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_app, name='main_app'),
    path('programs', views.all_programs, name='all_programs'),
    path('workout/<int:workout_id>', views.workout_detail, name='workout_detail'),
    path('affiliate-products', views.affiliate_page, name='affiliate_page'),
]
