# Generated by Django 5.0.3 on 2024-05-13 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0027_remove_dollpay_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='dollpay',
            name='arrival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='babydoll', to='ddms_app.arrival'),
        ),
    ]
