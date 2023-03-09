# Generated by Django 4.1.7 on 2023-03-09 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('nation', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
