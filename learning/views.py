
from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee


def home(request):
    employees = Employee.objects.all().order_by('id')

    return render(request, 'base.html', {
        'employees': employees
    })
def employee_detail(request,id):
    employee = get_object_or_404(Employee,id=id)

 
    return render(request,"employe_details.html",{'employee':employee})
def employee_edit(request,id):
    employee = get_object_or_404(Employee,id=id)
    if request.method =='POST':
        employee.first_name =request.POST.get("first_name",'').strip()
        employee.last_name=request.POST.get("last_name",'').strip()
        employee.email =request.POST.get('email','').strip()
        employee.designation = request.POST.get('designation', '').strip()
        try:
            employee.salary = int(request.POST.get('salary',''))
            employee.save
            return redirect('home')
        except(ValueError,TypeError):
            return render(request,"employe_edit.html",{
                'employe':employee,
                'error':"plz enter a valid salary"
            })
        return render(request, 'employee_edit.html', {'employee': employee})
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('home')

    return render(request, 'employee_delete.html', {'employee': employee})    





       


