# Generated by Django 2.2 on 2021-05-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoNinjaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
