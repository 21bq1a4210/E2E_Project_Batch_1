# Generated by Django 4.2.6 on 2024-01-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1),
        ),
    ]
