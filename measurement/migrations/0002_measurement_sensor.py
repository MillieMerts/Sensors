# Generated by Django 4.2.4 on 2023-09-17 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
