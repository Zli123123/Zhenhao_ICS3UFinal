# Generated by Django 3.2.6 on 2022-04-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]