# Generated by Django 4.2.2 on 2023-06-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0007_remove_employees_des_remove_employees_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]
