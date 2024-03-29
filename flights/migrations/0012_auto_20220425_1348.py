# Generated by Django 3.2.6 on 2022-04-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0011_auto_20220425_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'M'), ('female', 'F'), ('private', 'X')], default='private', max_length=8),
        ),
        migrations.AddField(
            model_name='passenger',
            name='ticketprice',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=6),
        ),
    ]
