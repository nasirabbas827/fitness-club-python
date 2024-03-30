from django.contrib import admin

from .models import Manager, Instructor, Workout,Customer, CustomerFeeReport, InstructorSalary, CustomerFitness, DailyFitnessReport

admin.site.register(Manager)
admin.site.register(Instructor)
admin.site.register(Workout)
admin.site.register(Customer)
admin.site.register(CustomerFeeReport)
admin.site.register(InstructorSalary)
admin.site.register(CustomerFitness)
admin.site.register(DailyFitnessReport)
