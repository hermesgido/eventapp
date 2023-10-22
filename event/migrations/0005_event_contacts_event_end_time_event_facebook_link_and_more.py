# Generated by Django 4.2.6 on 2023-10-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_eventbooking_qr_code_venuebooking_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contacts',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='map_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
    ]
