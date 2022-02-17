# Generated by Django 4.0.2 on 2022-02-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DOCTOR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('chamber_address', models.CharField(max_length=100)),
                ('registration_number', models.IntegerField()),
            ],
        ),
    ]
