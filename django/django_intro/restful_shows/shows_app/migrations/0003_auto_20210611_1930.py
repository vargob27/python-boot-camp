# Generated by Django 2.2 on 2021-06-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0002_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
