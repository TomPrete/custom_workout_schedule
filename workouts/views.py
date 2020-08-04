from django.shortcuts import render
from .models import Program, Workout, Category, Type, MuscleGroup
from .generate_schedule import Schedule

def main_app(request):
  programs = Program.objects.all()
  week = [3, 4, 5, 6, 7]
  if request.method == "POST":
    programs_selected = request.POST.getlist('programs')
    days = request.POST['days']
    program_workouts = _get_program_workouts(programs_selected)
    final_schedule = Schedule(program_workouts, days).assign_week_to_schedule()
    return render(request, 'workouts/home.html', {'programs': programs, 'week': week, 'schedule': final_schedule})
  return render(request, 'workouts/home.html', {'programs': programs, 'week': week})


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
  program_workouts = []
  return render(request, 'workouts/workout_detail.html', {'workout': workout})


def affiliate_page(request):
  return render(request, 'workouts/products.html', {})
