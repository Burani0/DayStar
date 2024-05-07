# Generated by Django 5.0.3 on 2024-05-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0015_alter_arrival_period_of_stay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Partial', 'Partial')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='departure',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Partial', 'Partial')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='departure',
            name='period_stayed',
            field=models.CharField(blank=True, choices=[('Halfday', 'Halfday'), ('Fullday', 'Fullday')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='NIN_number',
            field=models.CharField(max_length=30),
        ),
    ]