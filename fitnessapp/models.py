from django.db import models
import datetime

class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    qualification = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=100)
    workout_description = models.TextField()
    category_name = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE , default = 1)  # Add this line

    def __str__(self):
        return self.workout_name

    def __str__(self):
        return self.workout_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    workout_plan = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class CustomerFitness(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Assuming weight is in kilograms
    waist_measurement = models.DecimalField(max_digits=5, decimal_places=2)  # Assuming waist measurement is in centimeters
    height = models.DecimalField(max_digits=5, decimal_places=2)  # Assuming height is in meters
    goal = models.TextField()
    date = models.DateField(default=datetime.date(2023, 1, 
    1))

    @property
    def bmi(self):
        # Calculate BMI (BMI = weight (kg) / height^2 (m^2))
        height_meters = self.height  # Height is already in meters
        bmi = self.weight / (height_meters ** 2)
        return bmi

    def __str__(self):
        return f"BMI: {self.bmi} - Customer: {self.customer.name}"



class DailyFitnessReport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    exercise_duration = models.DurationField()  # Duration of exercise
    calories_burned = models.IntegerField()    # Calories burned during exercise
    water_consumed = models.DecimalField(max_digits=5, decimal_places=2)  # Water consumed during the day

    def __str__(self):
        return f"Report for {self.customer.name} on {self.date}"


class CustomerFeeReport(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('online', 'Online'),
        ('cash', 'Cash'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer.name} - {self.date}"
    


class InstructorSalary(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('online', 'Online'),
        ('cash', 'Cash'),
    ]
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    month = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.instructor.full_name} - {self.month}"
