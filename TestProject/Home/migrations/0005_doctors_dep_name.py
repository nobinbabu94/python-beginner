# Generated by Django 5.0.3 on 2024-03-27 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_departments_dep_name_alter_doctors_docs_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='dep_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.departments'),
        ),
    ]