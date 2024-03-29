# Generated by Django 3.2.6 on 2022-04-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20220425_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='destination_link',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='origin_link',
        ),
        migrations.AddField(
            model_name='airport',
            name='city_link',
            field=models.URLField(default='www.google.com', max_length=128),
        ),
    ]
