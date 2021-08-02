# Generated by Django 3.2.5 on 2021-07-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('episodes', models.IntegerField()),
                ('logo', models.CharField(max_length=250)),
                ('airing', models.BooleanField()),
                ('rating', models.DecimalField(decimal_places=3, max_digits=5)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
