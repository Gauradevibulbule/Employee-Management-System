from django.urls import path
from  . import views
urlpatterns = [
    path("",views.home, name='home'),
    path('create-employee/', views.createEmployeee, name="create_employee"),
    path('employee-list/', views.employee_list, name="employee_list"),
    path('employee-edit/<int:pid>', views.edit_employee, name="edit_employee"),
    path('delete_employee/<int:pid>', views.delete_employee, name="delete_employee"),
    path('leave-status/<int:pid>', views.leave_status, name="leave_status"),
]