# Generated by Django 4.2.6 on 2023-10-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_description_event_hosts_event_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbooking',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venuebooking',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
