# Generated by Django 5.0.3 on 2024-05-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0014_remove_arrival_sitter_assigned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='period_of_stay',
            field=models.CharField(blank=True, choices=[('Halfday', 'Halfday'), ('Fullday', 'Fullday')], max_length=20, null=True),
        ),
    ]
