# Generated by Django 5.0.2 on 2024-02-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_marks_delete_academics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marks',
            new_name='Academics',
        ),
    ]
