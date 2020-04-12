# Generated by Django 3.0.3 on 2020-04-07 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0002_auto_20200408_0105'),
        ('rank_app', '0003_auto_20200408_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='category_age',
        ),
        migrations.RemoveField(
            model_name='rank',
            name='category_gender',
        ),
        migrations.RemoveField(
            model_name='rank',
            name='category_name',
        ),
        migrations.AddField(
            model_name='rank',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category_app.Category'),
            preserve_default=False,
        ),
    ]
