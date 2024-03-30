from django import forms

class ManagerLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

from .models import Instructor

class InstructorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Instructor
        fields = ['username', 'full_name', 'password', 'email', 'phone_number', 'address', 'qualification', 'timings']
from .models import Workout

from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Workout
        fields = ['workout_name', 'workout_description', 'category_name', 'instructor'] 

from .models import Customer

class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Customer
        fields = ['name', 'email', 'password', 'phone_number', 'address', 'workout_plan']

from .models import CustomerFitness

class CustomerFitnessForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = CustomerFitness
        fields = ['customer', 'weight', 'waist_measurement', 'height', 'goal']

from .models import CustomerFeeReport

class CustomerFeeReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = CustomerFeeReport
        fields = ['customer', 'date', 'total_fee', 'amount_paid', 'payment_method', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

from .models import InstructorSalary

from django import forms
from .models import InstructorSalary

class InstructorSalaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = InstructorSalary
        fields = ['instructor', 'month', 'amount', 'payment_method', 'payment_date']
        widgets = {
            'month': forms.DateInput(attrs={'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }


from .models import DailyFitnessReport

class DailyFitnessReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = DailyFitnessReport
        fields = ['waist', 'weight', 'exercise_duration', 'calories_burned', 'water_consumed']  