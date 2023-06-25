from django.forms import ModelForm
from .models import *
from django import forms
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

from django import forms
from .models import Employee_leaves

class leaveform(forms.ModelForm):
    class Meta:
        model = Employee_leaves
        fields = [ 'from_date', 'to_date', 'leave_type', 'purpose']
        widgets = {
            
            'from_date': forms.DateInput(attrs={'class': 'form-control'}),
            'to_date': forms.DateInput(attrs={'class': 'form-control'}),
            'leave_type': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control'}),
        }

        


class createleaveform(forms.ModelForm):
    class Meta:
        model = Employee_leaves
        fields = ['employee', 'from_date', 'to_date', 'leave_type', 'purpose']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'leave_type': forms.Select(choices=Employee_leaves.leaves, attrs={'class': 'form-select'}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

