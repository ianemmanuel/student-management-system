# Generated by Django 4.0.5 on 2022-06-27 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_system', '0002_remove_adminhod_email_remove_adminhod_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]