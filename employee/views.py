from django.http import HttpResponse
from django.shortcuts import redirect, render
from employee.forms import EmployeeForm
from employee.models import Employee


# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee/employee_list.html', context)


def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    context = {'employee': employee}
    return render(request, 'employee/employee_detail.html', context)


def employee_create(request):
    if not request.user.is_authenticated:
        return HttpResponse("You are not authorized to create an employee.", status=403)

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, "employee/employee_create.html", {'form': form})

    form = EmployeeForm()
    return render(request, "employee/employee_create.html", {'form': form})
