from django.shortcuts import render, redirect , redirect, get_object_or_404
from django.contrib import messages
from .models import Manager, Instructor
from .forms import InstructorForm
from .models import Workout
from .forms import WorkoutForm
from .models import Customer
from .forms import CustomerForm
from .models import CustomerFitness
from .forms import CustomerFitnessForm
from .models import CustomerFeeReport
from .forms import CustomerFeeReportForm
from .models import InstructorSalary
from .forms import InstructorSalaryForm
from django.http import HttpResponse
import csv

def index(request):
    if 'manager_username' in request.session:
        return redirect('dashboard')  # Redirect to manager dashboard if manager is logged in

    if 'instructor_id' in request.session:
        return redirect('instructor_dashboard')  # Redirect to instructor dashboard if instructor is logged in

    # If neither manager nor instructor is logged in, render the index.html template
    return render(request, 'index.html')



def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            manager = Manager.objects.get(username=username, password=password)
            # If manager found, set session variable and redirect to dashboard
            request.session['manager_username'] = manager.username
            return redirect('dashboard')
        except Manager.DoesNotExist:
            # If manager not found, show error message
            messages.error(request, 'Invalid username or password')
    return render(request, 'manager_login.html')

def dashboard(request):
    # Get the logged-in manager's username from session
    username = request.session.get('manager_username', '')
    context = {
        'manager_username': username
    }
    return render(request, 'manager/manager_dashboard.html', context)

from django.http import HttpResponse
import subprocess

def backup(request):
    # Perform backup operation here
    try:
        # Example: Backup using Django's dumpdata command
        backup_file = 'backup.json'
        subprocess.run(['python', 'manage.py', 'dumpdata', '--output', backup_file])
        # Return a response indicating success
        return HttpResponse("Database backup successful. <a href='/'>Go back to homepage</a>")
    except Exception as e:
        # Return a response indicating failure
        return HttpResponse(f"Database backup failed: {str(e)}")
from django.shortcuts import redirect

def logout(request):
    if 'manager_username' in request.session:
        del request.session['manager_username']
    return redirect('home')

def add_instructor(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')

    manager_username = request.session['manager_username']  

    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor added successfully!')
            return redirect('view_instructors')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InstructorForm()
    return render(request, 'manager/add_instructor.html', {'form': form, 'manager_username': manager_username})


def view_instructors(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    instructors = Instructor.objects.all()
    return render(request, 'manager/view_instructors.html', {'instructors': instructors , 'manager_username': manager_username})

def edit_instructor(request, instructor_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    
    manager_username = request.session['manager_username']  
    

    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor updated successfully!')
            return redirect('view_instructors')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'manager/edit_instructor.html', {'form': form, 'instructor': instructor , 'manager_username': manager_username})

def delete_instructor(request, instructor_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        messages.success(request, 'Instructor deleted successfully!')
        return redirect('view_instructors')
    return render(request, 'manager/delete_instructor.html', {'instructor': instructor , 'manager_username': manager_username})


def add_workout(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout added successfully!')
            return redirect('view_workouts')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WorkoutForm()
    return render(request, 'manager/add_workout.html', {'form': form , 'manager_username': manager_username})

def view_workouts(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    workouts = Workout.objects.all()
    return render(request, 'manager/view_workouts.html', {'workouts': workouts , 'manager_username': manager_username})

def edit_workout(request, workout_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  

    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated successfully!')
            return redirect('view_workouts')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'manager/edit_workout.html', {'form': form, 'workout': workout , 'manager_username': manager_username})
def delete_workout(request, workout_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully!')
        return redirect('view_workouts')
    return render(request, 'manager/delete_workout.html', {'workout': workout , 'manager_username': manager_username})

def add_customer(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('view_customers')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerForm()
    return render(request, 'manager/add_customer.html', {'form': form  , 'manager_username': manager_username})

def view_customers(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customers = Customer.objects.all()
    return render(request, 'manager/view_customers.html', {'customers': customers  , 'manager_username': manager_username})

def edit_customer(request, customer_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('view_customers')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'manager/edit_customer.html', {'form': form, 'customer': customer  , 'manager_username': manager_username})

def delete_customer(request, customer_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('view_customers')
    return render(request, 'manager/delete_customer.html', {'customer': customer  , 'manager_username': manager_username})



def add_customer_fitness(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    if request.method == 'POST':
        form = CustomerFitnessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_customer_fitness')  
    else:
        form = CustomerFitnessForm()

    context = {
        'form': form,
        'manager_username': manager_username
    }
    return render(request, 'manager/add_customer_fitness.html', context)


def view_customer_fitness(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customer_fitness = CustomerFitness.objects.all()

    context = {
        'customer_fitness': customer_fitness,
        'manager_username': manager_username

    }
    return render(request, 'manager/view_customer_fitness.html', context)

from django.shortcuts import render, redirect
from .models import DailyFitnessReport
from .forms import DailyFitnessReportForm

def view_daily_report(request, customer_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    
    
    customer_fitness_reports = DailyFitnessReport.objects.filter(customer_id=customer_id)

    context = {
        'customer_fitness_reports': customer_fitness_reports,
                'manager_username': manager_username,

    }
    return render(request, 'manager/view_daily_report.html', context)


def edit_customer_fitness(request, id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customer_fitness = get_object_or_404(CustomerFitness, id=id)
    
    if request.method == 'POST':
        form = CustomerFitnessForm(request.POST, instance=customer_fitness)
        if form.is_valid():
            form.save()
            return redirect('view_customer_fitness')
    else:
        form = CustomerFitnessForm(instance=customer_fitness)

    context = {
        'form': form,
        'manager_username': manager_username

    }
    return render(request, 'manager/edit_customer_fitness.html', context)

def delete_customer_fitness(request, id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    customer_fitness = get_object_or_404(CustomerFitness, id=id)
    if request.method == 'POST':
        customer_fitness.delete()
        return redirect('view_customer_fitness')

    context = {
        'customer_fitness': customer_fitness,
        'manager_username': manager_username

    }
    return render(request, 'manager/delete_customer_fitness.html', context)

def add_customer_fee(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    if request.method == 'POST':
        form = CustomerFeeReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer fee report added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerFeeReportForm()
    return render(request, 'manager/add_customer_fee.html', {'form': form  , 'manager_username': manager_username})

from django.db.models import Q
from datetime import datetime


def view_customer_fees(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    search_date = request.GET.get('search_date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    customer_fees = CustomerFeeReport.objects.all()

    if search_date:
        customer_fees = customer_fees.filter(date=search_date)
    elif start_date and end_date:
        customer_fees = customer_fees.filter(date__range=(start_date, end_date))

    return render(request, 'manager/view_customer_fees.html', {'customer_fees': customer_fees , 'manager_username': manager_username})


import csv
from datetime import datetime
from django.http import HttpResponse
from .models import CustomerFeeReport

def export_customer_fees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer_fees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Customer', 'Date', 'Total Fee', 'Amount Paid', 'Payment Method', 'Notes'])

    search_date_from = request.GET.get('search_date_from')
    search_date_to = request.GET.get('search_date_to')

    if search_date_from and search_date_to:
        # Convert search dates to datetime objects
        search_date_from = datetime.strptime(search_date_from, '%Y-%m-%d')
        search_date_to = datetime.strptime(search_date_to, '%Y-%m-%d').replace(hour=23, minute=59, second=59)

        # Filter customer fees based on the date range
        customer_fees = CustomerFeeReport.objects.filter(date__range=[search_date_from, search_date_to])

        # Export only the filtered data
        for fee in customer_fees:
            writer.writerow([fee.customer.name, fee.date, fee.total_fee, fee.amount_paid, fee.payment_method, fee.notes])
    else:
        # If no search date range is provided, export all customer fees
        for fee in CustomerFeeReport.objects.all():
            writer.writerow([fee.customer.name, fee.date, fee.total_fee, fee.amount_paid, fee.payment_method, fee.notes])

    return response


def edit_customer_fee(request, fee_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    fee = get_object_or_404(CustomerFeeReport, pk=fee_id)
    if request.method == 'POST':
        form = CustomerFeeReportForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer fee report updated successfully!')
            return redirect('view_customer_fees')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerFeeReportForm(instance=fee)
    return render(request, 'manager/edit_customer_fee.html', {'form': form, 'fee': fee , 'manager_username': manager_username})

def delete_customer_fee(request, fee_id):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    fee = get_object_or_404(CustomerFeeReport, pk=fee_id)
    if request.method == 'POST':
        fee.delete()
        messages.success(request, 'Customer fee report deleted successfully!')
        return redirect('view_customer_fees')
    return render(request, 'manager/delete_customer_fee.html', {'fee': fee , 'manager_username': manager_username})

def add_instructor_salary(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    if request.method == 'POST':
        form = InstructorSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
    else:
        form = InstructorSalaryForm()
    return render(request, 'manager/add_instructor_salary.html', {'form': form , 'manager_username': manager_username})




def view_instructor_salaries(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')

    manager_username = request.session['manager_username']
    salaries = InstructorSalary.objects.all()

    # Handle filtering by date range
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if date_from and date_to:
        salaries = salaries.filter(payment_date__range=[date_from, date_to])

    context = {
        'salaries': salaries,
        'manager_username': manager_username,
    }
    return render(request, 'manager/view_instructor_salaries.html', context)

def export_salary_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="instructor_salaries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Instructor', 'Month', 'Amount', 'Payment Method', 'Payment Date'])

    # Filter salaries based on date range, if provided
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if date_from and date_to:
        salaries = InstructorSalary.objects.filter(payment_date__range=[date_from, date_to])
    else:
        salaries = InstructorSalary.objects.all()

    for salary in salaries:
        writer.writerow([salary.instructor.full_name, salary.month, salary.amount, salary.payment_method, salary.payment_date])

    return response

from django.db.models import Sum

from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import CustomerFeeReport, InstructorSalary

def view_profit(request):
    if 'manager_username' not in request.session:
        return redirect('manager_login')
    manager_username = request.session['manager_username']  
    

    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # Filter customer fees and instructor salaries based on the date range
    customer_fees = CustomerFeeReport.objects.filter(date__range=[date_from, date_to])
    instructor_salaries = InstructorSalary.objects.filter(payment_date__range=[date_from, date_to])

    # Calculate total income from customer fees
    total_income = customer_fees.aggregate(total_income=Sum('amount_paid'))['total_income'] or 0

    # Calculate total amount paid to instructors as salaries
    total_salaries = instructor_salaries.aggregate(total_salaries=Sum('amount'))['total_salaries'] or 0

    # Calculate profit
    profit = total_income - total_salaries

    context = {
        'total_income': total_income,
        'total_salaries': total_salaries,
        'profit': profit,
        'manager_username': manager_username
    }
    return render(request, 'manager/view_profit.html', context)


def instructor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            instructor = Instructor.objects.get(username=username, password=password)
            # Set session variable to indicate the user is logged in
            request.session['instructor_id'] = instructor.pk
            return redirect('instructor_dashboard')  # Redirect to the instructor dashboard
        except Instructor.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'instructor_login.html')


def instructor_dashboard(request):
    # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')

    # Pass instructor data to the template
    context = {
        'instructor': instructor,
        'instructor_id':instructor_id,
    }
    return render(request, 'instructor/instructor_dashboard.html', context)

from .models import Workout, Customer

from django.shortcuts import render, redirect
from .models import Workout, Customer, CustomerFitness

def calculate_bmi(weight, height):
    # Calculate BMI (BMI = weight (kg) / height^2 (m^2))
    height_meters = height
    bmi = weight / (height_meters ** 2)
    return bmi

def show_customers(request, workout_id):
    try:
        workout = Workout.objects.get(pk=workout_id)
        customers = Customer.objects.filter(workout_plan=workout)
    except Workout.DoesNotExist:
        pass

    for customer in customers:
        try:
            customer_fitness = CustomerFitness.objects.get(customer_id=customer.pk)
            bmi = calculate_bmi(customer_fitness.weight, customer_fitness.height)
            customer.customerfitness = {
                'weight': customer_fitness.weight,
                'waist_measurement': customer_fitness.waist_measurement,
                'height': customer_fitness.height,
                'bmi': bmi,
                'goal': customer_fitness.goal
            }
        except CustomerFitness.DoesNotExist:
            customer.customerfitness = None

    context = {
        'workout': workout,
        'customers': customers,
    }
    return render(request, 'instructor/show_customers.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, CustomerFitness
from .forms import CustomerFitnessForm

def add_report(request, customer_id):
     # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')
    
    customer = get_object_or_404(Customer, pk=customer_id)
    customer_fitness, created = CustomerFitness.objects.get_or_create(customer=customer)

    if request.method == 'POST':
        form = CustomerFitnessForm(request.POST, instance=customer_fitness)
        if form.is_valid():
            form.save()
            return redirect('show_customers', workout_id=customer.workout_plan.pk)
    else:
        form = CustomerFitnessForm(instance=customer_fitness)

    context = {
        'form': form,
        'customer': customer,
        'instructor_id':instructor_id,
    }
    return render(request, 'instructor/add_report.html', context)
from django.shortcuts import render, redirect
from .models import Customer, DailyFitnessReport
from .forms import DailyFitnessReportForm

def add_report(request, customer_id):
     # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        pass

    if request.method == 'POST':
        form = DailyFitnessReportForm(request.POST)
        if form.is_valid():
            # Save the report
            report = form.save(commit=False)
            report.customer = customer
            report.save()
            return redirect('show_customers', workout_id=customer.workout_plan.pk)
    else:
        form = DailyFitnessReportForm()

    context = {
        'form': form,
        'customer': customer,
        'instructor_id': instructor_id,
    }
    return render(request, 'instructor/add_report.html', context)


def instructor_logout(request):
    # Delete the instructor_id from the session if it exists
    if 'instructor_id' in request.session:
        del request.session['instructor_id']
    
    # Redirect the instructor to the login page after logout
    return redirect('home')


def instructor_add_customer_fee(request):
        # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')

    

    if request.method == 'POST':
        form = CustomerFeeReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer fee report added successfully!')
            return redirect('instructor_view_customer_fees')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerFeeReportForm()
    return render(request, 'instructor/add_customer_fee.html', {'form': form  , 'instructor_id': instructor_id})



def instructor_view_customer_fees(request):
        # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')

    

    search_date = request.GET.get('search_date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    customer_fees = CustomerFeeReport.objects.all()

    if search_date:
        customer_fees = customer_fees.filter(date=search_date)
    elif start_date and end_date:
        customer_fees = customer_fees.filter(date__range=(start_date, end_date))

    return render(request, 'instructor/view_customer_fees.html', {'customer_fees': customer_fees , 'instructor_id': instructor_id})


def export_customer_fees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer_fees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Customer', 'Date', 'Total Fee', 'Amount Paid', 'Payment Method', 'Notes'])

    search_date_from = request.GET.get('search_date_from')
    search_date_to = request.GET.get('search_date_to')

    if search_date_from and search_date_to:
        # Convert search dates to datetime objects
        search_date_from = datetime.strptime(search_date_from, '%Y-%m-%d')
        search_date_to = datetime.strptime(search_date_to, '%Y-%m-%d').replace(hour=23, minute=59, second=59)

        # Filter customer fees based on the date range
        customer_fees = CustomerFeeReport.objects.filter(date__range=[search_date_from, search_date_to])

        # Export only the filtered data
        for fee in customer_fees:
            writer.writerow([fee.customer.name, fee.date, fee.total_fee, fee.amount_paid, fee.payment_method, fee.notes])
    else:
        # If no search date range is provided, export all customer fees
        for fee in CustomerFeeReport.objects.all():
            writer.writerow([fee.customer.name, fee.date, fee.total_fee, fee.amount_paid, fee.payment_method, fee.notes])

    return response


def instructor_edit_customer_fee(request, fee_id):
        # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')

    

    fee = get_object_or_404(CustomerFeeReport, pk=fee_id)
    if request.method == 'POST':
        form = CustomerFeeReportForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer fee report updated successfully!')
            return redirect('instructor_view_customer_fees')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerFeeReportForm(instance=fee)
    return render(request, 'instructor/edit_customer_fee.html', {'form': form, 'fee': fee , 'instructor_id': instructor_id})

def instructor_delete_customer_fee(request, fee_id):
        # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')
 
    

    fee = get_object_or_404(CustomerFeeReport, pk=fee_id)
    if request.method == 'POST':
        fee.delete()
        messages.success(request, 'Customer fee report deleted successfully!')
        return redirect('instructor_view_customer_fees')
    return render(request, 'instructor/delete_customer_fee.html', {'fee': fee , 'instructor_id': instructor_id})

def instructor_view_profit(request):
        # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']
    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        # If the instructor does not exist, log them out and redirect to login page
        del request.session['instructor_id']
        return redirect('instructor_login')


    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # Filter customer fees and instructor salaries based on the date range
    customer_fees = CustomerFeeReport.objects.filter(date__range=[date_from, date_to])
    instructor_salaries = InstructorSalary.objects.filter(payment_date__range=[date_from, date_to])

    # Calculate total income from customer fees
    total_income = customer_fees.aggregate(total_income=Sum('amount_paid'))['total_income'] or 0

    # Calculate total amount paid to instructors as salaries
    total_salaries = instructor_salaries.aggregate(total_salaries=Sum('amount'))['total_salaries'] or 0

    # Calculate profit
    profit = total_income - total_salaries

    context = {
        'total_income': total_income,
        'total_salaries': total_salaries,
        'profit': profit,
        'instructor_id': instructor_id,
    }
    return render(request, 'instructor/view_profit.html', context)

def view_salary(request):
    # Check if instructor is logged in
    if 'instructor_id' not in request.session:
        return redirect('instructor_login')  # Redirect to login page if not logged in
    
    # Retrieve instructor object from session
    instructor_id = request.session['instructor_id']

    # Retrieve all salary records for the logged-in instructor
    instructor_salary_records = InstructorSalary.objects.filter(instructor_id=instructor_id)

    # Calculate total salary
    total_salary = sum(record.amount for record in instructor_salary_records)

    # Pass data to the template
    context = {
        'instructor_salary_records': instructor_salary_records,
        'total_salary': total_salary,
        'instructor_id': instructor_id,
    }

    return render(request, 'instructor/view_salary.html', context)