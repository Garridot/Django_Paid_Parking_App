# Generated by Django 3.2.6 on 2021-10-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_alter_parking_ticket_checkin_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_ticket',
            name='checkin_time',
            field=models.DateTimeField(verbose_name='Check In Time'),
        ),
    ]
