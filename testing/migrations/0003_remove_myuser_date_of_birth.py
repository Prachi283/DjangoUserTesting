# Generated by Django 4.0.2 on 2022-03-09 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_myuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
    ]
