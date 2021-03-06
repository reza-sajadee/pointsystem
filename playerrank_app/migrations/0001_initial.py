# Generated by Django 3.0.3 on 2020-04-08 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('result_app', '0002_result_point'),
        ('rank_app', '0006_auto_20200408_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='playerRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('best', models.IntegerField()),
                ('rank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rank_app.Rank')),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result_app.Result')),
            ],
        ),
    ]
