# Generated by Django 4.2 on 2023-04-25 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_department_departments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departments',
            new_name='Department',
        ),
    ]
