# Generated by Django 5.0.3 on 2024-05-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0035_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='sitter_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
