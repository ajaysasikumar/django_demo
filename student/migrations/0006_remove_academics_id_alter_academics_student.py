# Generated by Django 5.0.2 on 2024-02-09 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_studentinfo_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academics',
            name='id',
        ),
        migrations.AlterField(
            model_name='academics',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='student.studentinfo'),
        ),
    ]
