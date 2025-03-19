from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project_detail_all/', views.project_detail_all, name='project_detail_all'),
]