# Generated by Django 5.0.3 on 2024-03-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_doc_image_doctors_docs_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dep_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='docs_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='docs_spec',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
