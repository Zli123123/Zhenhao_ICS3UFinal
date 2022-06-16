# Generated by Django 3.2.6 on 2022-04-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_airport_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passaengers', to='flights.Flight')),
            ],
        ),
    ]