

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
    path('employee/<int:id>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:id>/delete/', views.employee_delete, name='employee_delete'),
]

