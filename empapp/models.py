from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.CharField(max_length=200)
    employeeID = models.CharField(max_length=200,editable=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    salary = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.employeeID:  # Only generate employeeID for new instances
            last_object = self.__class__.objects.last()  # Get the last object in the class
            if last_object:
                last_id = int(last_object.id)
                emp_id = str(last_id + 1)
            else:
                emp_id = '1'
            self.employeeID = 'EMP ' + emp_id
        super().save(*args, **kwargs)
    def __str__(self):
        return self.employee



class Designation(models.Model):
    Designation_Types = (
        ('CEO', 'CEO'),
        ('HR', 'HR'),
        ('Backend Developer', 'Backend Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Quality Analyst', 'Quality Analyst'),
        ('BD', 'BD'),
    )
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, choices=Designation_Types)


    def __str__(self):
        return self.get_designation_display()


class Team(models.Model):
    Team_types = (
        ('Management', 'Management'),
        ('Wordpress', 'Wordpress'),
        ('Python', 'Python'),
        ('UI/UX', 'UI/UX'),
        ('QA', 'QA'),
    )
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE)
    team = models.CharField(max_length=20, choices=Team_types)

    def __str__(self):
        return str(self.employee)


class Employee_leaves(models.Model):
    leaves = (
        ('Half day', 'Half day'),
        ('Full day', 'Full day')

    )
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    leave_type = models.CharField(max_length=300, choices=leaves)
    purpose=models.TextField()

    def __str__(self):
        return str(self.employee)
