# Generated by Django 5.0.2 on 2024-02-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('Class', models.CharField(max_length=3)),
                ('Place', models.CharField(max_length=300)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]
