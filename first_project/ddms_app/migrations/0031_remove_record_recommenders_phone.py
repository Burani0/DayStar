# Generated by Django 5.0.3 on 2024-05-18 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0030_procurement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='recommenders_phone',
        ),
    ]
