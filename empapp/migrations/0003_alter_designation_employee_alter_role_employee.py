# Generated by Django 4.2.2 on 2023-06-22 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_remove_employees_designation_remove_employees_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empapp.employees'),
        ),
        migrations.AlterField(
            model_name='role',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empapp.employees'),
        ),
    ]
