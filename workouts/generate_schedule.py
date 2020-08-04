from .models import Category, Workout
from django.db.models import Q
from .program_config import schedule
import random

class Schedule:
  def __init__(self, program_workouts, days):
    self.workouts = program_workouts
    self.days = days
    self.schedule = []


  # Assign a workout for each day of week
  def get_workouts_per_week(self):
    days_per_week = schedule[self.days]
    week = {}
    for key in days_per_week:
      random.shuffle(days_per_week[key])
      category_type = days_per_week[key][0]
      workout = self.assign_workout_to_day(category_type)
      week[key] = workout
    return week

  # Get a workout for a day
  def assign_workout_to_day(self, category_type):
      category = Category.objects.get(category_name=category_type)
      available_workouts_in_category = self.workouts.filter(category=category)
      workout = available_workouts_in_category.order_by('?').first()
      return workout

  def assign_week_to_schedule(self):
    for i in range(12):
      individual_week = self.get_workouts_per_week()
      self.schedule.append(individual_week)
    return self.schedule
