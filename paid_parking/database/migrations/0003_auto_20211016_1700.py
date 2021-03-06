# Generated by Django 3.2.6 on 2021-10-16 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20211016_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=50, verbose_name='License Plate')),
                ('resident', models.CharField(max_length=100, verbose_name='Resident')),
            ],
        ),
        migrations.AlterField(
            model_name='total_amount',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.car', verbose_name='Cars'),
        ),
    ]
