from django.contrib import admin
from .models import Employee, Department


# Register your models here.
# list display for Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'Dob', 'department', 'age')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
