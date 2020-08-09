from django.contrib import admin
from .models import Program, Workout, Category, Type, MuscleGroup, Message, ScheduleDetail, Schedule

all_models = [Program, Workout, Category, Type, MuscleGroup, Message, ScheduleDetail, Schedule]

admin.site.register(all_models)
