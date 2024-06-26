# Generated by Django 5.0.3 on 2024-05-06 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0021_alter_departure_arrival'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailypay',
            name='shift_attended',
        ),
        migrations.RemoveField(
            model_name='monthlypay',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='monthlypay',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='monthlypay',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='monthlypay',
            name='departure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mpays', to='ddms_app.departure'),
        ),
    ]
