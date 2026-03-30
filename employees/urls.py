from django.urls import path
from . import views

urlpatterns = [
    path('',            views.employee_dashboard, name='employee_dashboard'),
    path('employee/<int:pk>/', views.employee_dashboard, name='employee_dashboard'),
    path('add/',        views.add_employee,        name='add_employee'),
]