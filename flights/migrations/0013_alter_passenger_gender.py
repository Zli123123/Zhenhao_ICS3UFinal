# Generated by Django 3.2.6 on 2022-04-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_auto_20220425_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('private', 'Private')], default='private', max_length=8),
        ),
    ]
