# Generated by Django 3.0.8 on 2020-08-07 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_remove_scheduledetail_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(validators=[django.core.validators.MaxLengthValidator(1000)])),
            ],
        ),
    ]
