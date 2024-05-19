# Generated by Django 5.0.3 on 2024-05-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0033_remove_sitter_on_duty_sitter_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrival',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arrival',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='arrival',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
