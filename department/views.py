from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Department

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()

    return render(request, 'department/department_form.html', {'form': form})
