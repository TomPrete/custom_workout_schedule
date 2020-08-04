from django.contrib import admin
from .models import Program, Workout, Category, Type, MuscleGroup

all_models = [Program, Workout, Category, Type, MuscleGroup]

admin.site.register(all_models)
