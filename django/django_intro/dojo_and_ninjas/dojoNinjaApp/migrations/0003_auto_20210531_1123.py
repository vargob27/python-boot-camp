# Generated by Django 2.2 on 2021-05-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoNinjaApp', '0002_dojo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='description',
            field=models.TextField(default=''),
        ),
    ]