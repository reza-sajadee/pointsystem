# Generated by Django 3.0.3 on 2020-04-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]