from django.db import models
from django.core.validators import MaxLengthValidator

class Program(models.Model):
    program = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.program}"

class Workout(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=50)
    time = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    workouts = models.ManyToManyField(Workout, related_name='category')

    def __str__(self):
        return f"{self.category_name}"

class Type(models.Model):
    type = models.CharField(max_length=20)
    workouts = models.ManyToManyField(Workout)

    def __str__(self):
        return f"{self.type}"

class MuscleGroup(models.Model):
    group = models.CharField(max_length=20, blank=True, null=True)
    workouts = models.ManyToManyField(Workout)

    def __str__(self):
        return f"{self.group}"

class Schedule(models.Model):
    count = models.IntegerField(default=1)

class ScheduleDetail(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule_detail')
    week = models.IntegerField()
    day = models.CharField(max_length=6)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='schedule_workouts', null=True, blank=True)

class Message(models.Model):
    email = models.EmailField(max_length=100)
    message = models.TextField(validators=[MaxLengthValidator(1000)])

    def __str__(self):
        return f"Email: {email}, Message: {message}"
