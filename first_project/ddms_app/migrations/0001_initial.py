# Generated by Django 5.0.4 on 2024-04-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_person', models.CharField(blank=True, max_length=50, null=True)),
                ('person_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('time_in', models.DateTimeField(auto_now_add=True, null=True)),
                ('period_of_stay', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('sitter_assigned', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Surname', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('any_allegies', models.CharField(blank=True, max_length=50, null=True)),
                ('any_ongoing_medication', models.CharField(blank=True, max_length=50)),
                ('language_understood', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_person', models.CharField(blank=True, max_length=50, null=True)),
                ('person_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('time_out', models.DateTimeField(auto_now_add=True, null=True)),
                ('period_stayed', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('location', models.CharField(max_length=30)),
                ('next_of_kin', models.CharField(max_length=50)),
                ('next_of_kin_phone', models.CharField(max_length=15)),
                ('NIN_number', models.IntegerField(default=0)),
                ('recommenders_name', models.CharField(max_length=50)),
                ('recommenders_phone', models.CharField(max_length=15)),
                ('religion', models.CharField(max_length=20)),
                ('level_of_education', models.CharField(max_length=20)),
                ('sitter_number', models.IntegerField(default=0)),
                ('phone_number', models.IntegerField(default=0)),
            ],
        ),
    ]
