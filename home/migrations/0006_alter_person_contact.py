# Generated by Django 5.1.1 on 2024-09-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_excelupload_person_delete_excelfileupload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
