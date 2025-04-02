# Generated by Django 5.1.7 on 2025-03-24 21:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('teachers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.subject'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentprofile'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student', 'date')},
        ),
    ]
