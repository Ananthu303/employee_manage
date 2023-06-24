from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render
from .models import Employees


@login_required(login_url='login')
def index(request):
    employees = Employees.objects.all()

    return render(request, 'index.html', {"a": employees})


def login_admin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        useradmin = user
        employee = request.POST['employee']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        salary = request.POST['salary']
        phone = request.POST['phone']
        create = Employees(user=useradmin, employee=employee, firstname=firstname, lastname=lastname, email=email,
                           salary=salary, phonenumber=phone)
        create.save()
        return redirect('index')


    else:
        form = empform()

    return render(request, 'create.html', {'form': form})


@login_required(login_url='login')
def edit(request, id):
    a = Employees.objects.get(id=id)
    print('xxxx')

    if request.method == 'POST':
        print('dddd')
        user = User.objects.get(id=request.user.id)
        employee = request.POST['employee']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        salary = request.POST['salary']
        phone = request.POST['phone']
        a.user = user
        a.employee = employee
        a.firstname = firstname
        a.lastname = lastname
        a.email = email
        a.salary = salary
        a.phonenumber = phone
        print('sss')
        a.save()
        return redirect('index')

    return render(request, 'edit.html', {'a': a})


@login_required(login_url='login')
def delete(request, id):
    a = Employees.objects.get(id=id)
    a.delete()
    return redirect('index')


@login_required(login_url='login')
def edit_designation(request, id):
    a = Employees.objects.get(id=id)
    try:
        b = Designation.objects.get(employee=a)
    except:
        b = Designation(employee=a)
        b.save()
    form = desform(instance=b)
    if request.method == 'POST':
        F = desform(request.POST, instance=b)
        if F.is_valid():
            F.save()
            return redirect('index')
    return render(request, 'edit_des.html', {'form': form})


@login_required(login_url='login')
def delete_designation(request, id):
    a = Employees.objects.get(id=id)
    try:
        b = Designation.objects.get(employee=a)
        b.delete()
    except:
        return HttpResponse('Role doesnt Exist')
    return redirect('index')


@login_required(login_url='login')
def edit_role(request, id):
    a = Employees.objects.get(id=id)
    try:
        b = Team.objects.get(employee=a)
    except:
        b = Team(employee=a)
        b.save()
    form = roleform(instance=b)
    if request.method == 'POST':
        F = roleform(request.POST, instance=b)
        if F.is_valid():
            F.save()
            return redirect('index')
    return render(request, 'editrole.html', {'form': form})


@login_required(login_url='login')
def delete_role(request, id):
    a = Employees.objects.get(id=id)
    b = Team.objects.get(employee=a)
    b.delete()
    return redirect('index')


@login_required(login_url='login')
def leaveapply(request):
    a = Employee_leaves.objects.all()
    return render(request, 'alleaves.html', {'a': a})


@login_required(login_url='login')
def create_leave(request):
    form = createleaveform()
    # email = 'overthinker740@gmail.com'
    if request.method == 'POST':
        form = createleaveform(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            purpose = form.cleaned_data['purpose']
            leave_type = form.cleaned_data['leave_type']
            # send_mail_hr(email, employee, from_date, to_date, purpose)
            form.save()
            return redirect('leave_all')
    return render(request, 'create_leave.html', {'form': form})


@login_required(login_url='login')
def edit_leave(request, id):
    a = Employee_leaves.objects.get(id=id)
    form = leaveform(instance=a)
    if request.method == 'POST':
        form = leaveform(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return redirect('leave_all')
    return render(request, 'edit_leave.html', {'form': form})


@login_required(login_url='login')
def delete_leave(request, id):
    a = Employee_leaves.objects.get(id=id)
    a.delete()
    return redirect('leave_all')


def send_mail_hr(email, employee, from_date, to_date, purpose):
    subject = "Leave Applied"
    message = f'Hi,{employee} is on leave from {from_date} to {to_date} due to {purpose}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


def salary(request):
    total = 0.0
    employees = Employees.objects.all()
    for employee in employees:
        total += float(employee.salary)

    return render(request, 'salary_graph.html', {'total_salary': total})

