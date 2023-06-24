
The Employee Management System is a Django application that allows you to manage employees, their designations, teams, and leaves. This document provides an overview of the models included in the system and their functionality.

Models
Employees
The Employees model represents the employees in the system. It has the following fields:

user: A foreign key to the User model from Django's authentication system.
employee: A character field representing the employee's name.
employeeID: A character field representing the unique employee ID (automatically generated).
firstname: A character field representing the employee's first name.
lastname: A character field representing the employee's last name.
email: An email field representing the employee's email address.
salary: A character field representing the employee's salary.
phonenumber: A character field representing the employee's phone number.
The Employees model also overrides the save method to automatically generate the employeeID when a new instance is created. If the employeeID is not already set, it generates a new ID based on the last ID in the database and increments it by one.

Designation
The Designation model represents the designations of employees. It has the following fields:

employee: A one-to-one relationship with the Employees model.
designation: A character field representing the employee's designation. It has predefined choices such as CEO, HR, Backend Developer, Frontend Developer, Quality Analyst, and BD.
Team
The Team model represents the teams to which employees belong. It has the following fields:

employee: A one-to-one relationship with the Employees model.
team: A character field representing the employee's team. It has predefined choices such as Management, Wordpress, Python, UI/UX, and QA.
Employee_leaves
The Employee_leaves model represents the leaves taken by employees. It has the following fields:

employee: A foreign key to the Employees model.
from_date: A DateField representing the start date of the leave.
to_date: A DateField representing the end date of the leave.
leave_type: A character field representing the type of leave (e.g., Half day or Full day).
purpose: A TextField representing the purpose or reason for taking the leave.
Usage
You can use the Employee Management System to perform the following actions:

Create, update, and delete employees.
Assign designations to employees.
Assign teams to employees.
Track and manage employee leaves.

