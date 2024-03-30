from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),  
    path('add-instructor/', views.add_instructor, name='add_instructor'),
    path('view_instructors/', views.view_instructors, name='view_instructors'),
    path('edit_instructor/<int:instructor_id>/', views.edit_instructor, name='edit_instructor'),
    path('delete_instructor/<int:instructor_id>/', views.delete_instructor, name='delete_instructor'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('view_workouts/', views.view_workouts, name='view_workouts'),
    path('edit_workout/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('delete_workout/<int:workout_id>/', views.delete_workout, name='delete_workout'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('add_customer_fitness/', views.add_customer_fitness, name='add_customer_fitness'),
    path('view_customer_fitness/', views.view_customer_fitness, name='view_customer_fitness'),
    path('edit_customer_fitness/<int:id>/', views.edit_customer_fitness, name='edit_customer_fitness'),
    path('delete_customer_fitness/<int:id>/', views.delete_customer_fitness, name='delete_customer_fitness'),
    path('add_customer_fee/', views.add_customer_fee, name='add_customer_fee'),
    path('view_customer_fees/', views.view_customer_fees, name='view_customer_fees'),
    path('edit_customer_fee/<int:fee_id>/', views.edit_customer_fee, name='edit_customer_fee'),
    path('delete_customer_fee/<int:fee_id>/', views.delete_customer_fee, name='delete_customer_fee'),
    path('export_customer_fees_csv/', views.export_customer_fees_csv, name='export_customer_fees_csv'),
    path('add_instructor_salary/', views.add_instructor_salary, name='add_instructor_salary'),
    path('view_instructor_salaries/', views.view_instructor_salaries, name='view_instructor_salaries'),
    path('export_salary_csv/', views.export_salary_csv, name='export_salary_csv'),
    path('view_profit/', views.view_profit, name='view_profit'),
    path('instructor-login/', views.instructor_login, name='instructor_login'),
    path('instructor-dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('show_customers/<int:workout_id>/', views.show_customers, name='show_customers'),
    path('add_report/<int:customer_id>/', views.add_report, name='add_report'),
    path('instructor-logout/', views.instructor_logout, name='instructor_logout'),
    path('instructor_add_customer_fee/', views.instructor_add_customer_fee, name='instructor_add_customer_fee'),
    path('instructor_view_customer_fees/', views.instructor_view_customer_fees, name='instructor_view_customer_fees'),
    path('instructor_edit_customer_fee/<int:fee_id>/', views.instructor_edit_customer_fee, name='instructor_edit_customer_fee'),
    path('instructor_delete_customer_fee/<int:fee_id>/', views.instructor_delete_customer_fee, name='instructor_delete_customer_fee'),
    path('instructor_view_profit/', views.instructor_view_profit, name='instructor_view_profit'),
    path('view-daily-report/<int:customer_id>/', views.view_daily_report, name='view_daily_report'),
    path('view_salary/', views.view_salary, name='view_salary'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)