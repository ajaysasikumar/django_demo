# Generated by Django 5.0.2 on 2024-02-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_studentinfo_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
