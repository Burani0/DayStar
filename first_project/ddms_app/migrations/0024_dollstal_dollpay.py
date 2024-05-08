# Generated by Django 5.0.3 on 2024-05-08 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddms_app', '0023_sitter_on_duty_time_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dollstal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dollpay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pricedoll', to='ddms_app.arrival')),
                ('dollstal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dollpays', to='ddms_app.dollstal')),
            ],
        ),
    ]