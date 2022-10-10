# Generated by Django 4.1.1 on 2022-10-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60)),
                ('weather_condition', models.CharField(max_length=500)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('minimum_temp', models.FloatField()),
                ('maximum_temp', models.FloatField()),
                ('icon', models.CharField(max_length=60)),
                ('cod', models.CharField(max_length=60)),
            ],
        ),
    ]
