# Generated by Django 4.2 on 2023-04-25 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_departments_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('doc_spec', models.CharField(max_length=255)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
    ]
