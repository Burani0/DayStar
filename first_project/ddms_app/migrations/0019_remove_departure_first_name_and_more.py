# Generated by Django 5.0.3 on 2024-05-06 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0018_remove_sitter_payment_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departure',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='departure',
            name='last_name',
        ),
        migrations.AddField(
            model_name='departure',
            name='arrival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='ddms_app.arrival'),
        ),
    ]
