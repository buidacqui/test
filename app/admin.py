from django.contrib import admin
from .models import Employee, Project

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'email', 'phone')  # Hiển thị cột trong Admin
    search_fields = ('name', 'email')  # Cho phép tìm kiếm
    list_filter = ('position',)  # Bộ lọc bên cạnh

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
