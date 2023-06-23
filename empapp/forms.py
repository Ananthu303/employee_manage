from django.forms import ModelForm
from .models import *


class empform(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class desform(ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'
        exclude = ('employee',)


class roleform(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ('employee',)


class leaveform(ModelForm):
    class Meta:
        model = Employee_leaves
        fields = '__all__'
        exclude = ('employee',)


class createleaveform(ModelForm):
    class Meta:
        model = Employee_leaves
        fields = '__all__'
