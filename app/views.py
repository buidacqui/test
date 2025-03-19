from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from . models import Employee, Project
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'app/employee.html', {'employees': employees})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'app/projects.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'app/project_detail.html', {'project': project})

def project_detail_all(request):
    projects = Project.objects.all()
    return render(request, 'app/project_detail_all.html', {'projects': projects})