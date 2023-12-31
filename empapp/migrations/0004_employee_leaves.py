# Generated by Django 4.2.2 on 2023-06-22 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0003_alter_designation_employee_alter_role_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('leave_type', models.CharField(choices=[('Half day', 'Half day'), ('Full day', 'Full day')], max_length=300)),
                ('purpose', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.employees')),
            ],
        ),
    ]
