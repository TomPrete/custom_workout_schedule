from django.shortcuts import render
from django.http import HttpResponse
from .models import Program, Workout, Category, Type, MuscleGroup
from .generate_schedule import Schedule
from collections import Counter
import csv
from ast import literal_eval

def main_app(request):
  programs = Program.objects.all()
  week = [3, 4, 5, 6, 7]
  final_schedule = None
  if request.method == "POST":
    programs_selected = request.POST.getlist('programs')
    if len(programs_selected) == 0:
      error_message = 'Please select at least 1 workout program.'
      return render(request, 'workouts/home.html', {'programs': programs, 'week': week, 'error': error_message})
    days = request.POST['days']
    program_workouts = _get_program_workouts(programs_selected)
    final_schedule = Schedule(program_workouts, days).assign_week_to_schedule()
    return render(request, 'workouts/home.html', {'programs': programs, 'week': week, 'schedule': final_schedule})
  return render(request, 'workouts/home.html', {'programs': programs, 'week': week})

def save_workout_to_csv(request, schedule):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="custom_workout_schedule.csv"'
  print(request)
  print(response)
  schedule.replace('%20', ' ')
  schedule = literal_eval(schedule)
  print(schedule)
  writer = csv.writer(response)
  writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
  writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

  return response
  # with open('custom_workout_schedule.csv', mode='w') as schedule_file:
  #   fieldnames = ['week', 'day', 'workout', 'program', 'minutes', 'categories']
  #   writer = csv.DictWriter(schedule_file, fieldnames=fieldnames)
  #   writer.writeheader()
  #   for index, value in enumerate(final_schedule):
  #     for key in value:
  #       writer.writerow({
  #         'week': index+1,
  #         'day': key,
  #         'workout': value[key],
  #         'program': value[key].program,
  #         'minutes': value[key].time
  #       })

def _get_program_workouts(programs):
  workouts = Program.objects.get(program=programs[0]).workouts.all()
  for program in programs[1:]:
    workouts = workouts | Program.objects.get(program=program).workouts.all()
  return workouts

def all_programs(request):
  all_programs = Program.objects.all().order_by('id')
  program_workouts = []
  for program in all_programs:
    workouts = program.workouts.all()
    total_workouts = workouts.count()
    program_workouts.append({
      'program': program,
      'workouts': workouts,
      'total_workouts': total_workouts
    })
  return render(request, 'workouts/programs_table.html', {'program_workouts': program_workouts})

def workout_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  related_workouts = _find_related_workouts(workout)
  return render(request, 'workouts/workout_detail.html', {'workout': workout, 'related_workouts': related_workouts})

# Get related workouts based on categories
def _find_related_workouts(workout):
  workouts_query = []
  list_of_workouts_in_category = []
  related_workouts = []
  if workout.category.all().count() == 1:
    list_of_workouts_in_category = workout.category.first().workouts.all()
    for related_workout in list_of_workouts_in_category:
      if related_workout != workout:
        related_workouts.append(related_workout)
  else:
    for category in workout.category.all():
      workouts_query.append(category.workouts.all())
    for list in workouts_query:
      for related_workout in list:
        list_of_workouts_in_category.append(related_workout)
    list_of_workouts_in_category = [k for k,v in Counter(list_of_workouts_in_category).items() if v>1]
    for related_workout in list_of_workouts_in_category:
        if related_workout != workout:
          related_workouts.append(related_workout)
  return related_workouts

def all_workouts(request):
  workouts = Workout.objects.all().order_by()
  return render(request, 'workouts/all_workouts.html', {'all_workouts': workouts})



def category_detail(request, category_id):
  category = Category.objects.get(id=category_id)
  all_workouts_in_category = Category.objects.get(id=category_id).workouts.all()
  return render(request, 'workouts/category_detail.html', {'category': category, 'all_workouts_in_category': all_workouts_in_category})


def affiliate_page(request):
  return render(request, 'workouts/products.html', {})
