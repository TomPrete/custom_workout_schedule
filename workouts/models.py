from django.db import models

class Program(models.Model):
    program = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.program}"

class Workout(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=50)
    time = models.IntegerField()

    def __str__(self):
        return f"{self.name} in {self.program}"

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
