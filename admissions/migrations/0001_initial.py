# Generated by Django 5.0.2 on 2025-04-04 21:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('applying_for_grade', models.CharField(max_length=10)),
                ('parent_first_name', models.CharField(max_length=100)),
                ('parent_last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('previous_school', models.CharField(blank=True, max_length=200, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('documents', models.FileField(blank=True, null=True, upload_to='admission_documents/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('reviewing', 'Under Review'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
