# Generated by Django 3.2.6 on 2022-03-31 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20220331_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='origin',
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
