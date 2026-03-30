from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee
import cloudinary
import os

def employee_dashboard(request, pk=None):
    employees = Employee.objects.all()

    if not employees.exists():
        return redirect('add_employee')

    if pk:
        emp = get_object_or_404(Employee, pk=pk)
    else:
        emp = employees.first()

    if request.method == 'POST':
        section = request.POST.get('section')

        if section == 'employee':
            emp.email      = request.POST.get('email', emp.email)
            emp.phone      = request.POST.get('phone', emp.phone)
            emp.role       = request.POST.get('role', emp.role)
            emp.department = request.POST.get('department', emp.department)
            emp.emp_type   = request.POST.get('emp_type', emp.emp_type)
            emp.join_date  = request.POST.get('join_date') or emp.join_date

        elif section == 'personal':
            emp.first_name  = request.POST.get('first_name', emp.first_name)
            emp.last_name   = request.POST.get('last_name', emp.last_name)
            emp.dob         = request.POST.get('dob') or emp.dob
            emp.gender      = request.POST.get('gender', emp.gender)
            emp.blood_group = request.POST.get('blood_group', emp.blood_group)
            emp.address     = request.POST.get('address', emp.address)

        elif section == 'additional':
            emp.education = request.POST.get('education', emp.education)
            emp.skills    = request.POST.get('skills', emp.skills)
            emp.hobbies   = request.POST.get('hobbies', emp.hobbies)
            emp.biotag    = request.POST.get('biotag', emp.biotag)

        elif section == 'emergency':
            emp.ec_name     = request.POST.get('ec_name', emp.ec_name)
            emp.ec_relation = request.POST.get('ec_relation', emp.ec_relation)
            emp.ec_phone    = request.POST.get('ec_phone', emp.ec_phone)
            emp.ec_alt_phone= request.POST.get('ec_alt_phone', emp.ec_alt_phone)

        elif section == 'photo':
            if request.FILES.get('photo'):
                file = request.FILES['photo']
                upload = cloudinary.uploader.upload(file, folder='employee_photos')
                emp.photo = upload['secure_url']

        emp.save()
        messages.success(request, 'Changes saved successfully.')
        return redirect('employee_dashboard', pk=emp.pk)

    context = {
        'emp': emp,
        'users': employees,
        'skills_list':  [s.strip() for s in emp.skills.split(',') if s.strip()],
        'hobbies_list': [h.strip() for h in emp.hobbies.split(',') if h.strip()],
        }
    return render(request, 'employees/employee_dashboard.html', context)


def add_employee(request):
    print("CLOUD_NAME:", os.environ.get('CLOUDINARY_CLOUD_NAME'))
    print("API_KEY:", os.environ.get('CLOUDINARY_API_KEY'))
    print("DEFAULT_FILE_STORAGE:", os.environ.get('DEFAULT_FILE_STORAGE'))
    print("CLOUD NAME:", cloudinary.config().cloud_name)

    if request.method == 'POST':
        emp = Employee(
            first_name  = request.POST.get('first_name'),
            last_name   = request.POST.get('last_name'),
            email       = request.POST.get('email'),
            phone       = request.POST.get('phone', ''),
            role        = request.POST.get('role'),
            department  = request.POST.get('department', ''),
            emp_type    = request.POST.get('emp_type', ''),
            join_date   = request.POST.get('join_date') or None,
            dob         = request.POST.get('dob') or None,
            gender      = request.POST.get('gender', ''),
            blood_group = request.POST.get('blood_group', ''),
            address     = request.POST.get('address', ''),
            education   = request.POST.get('education', ''),
            skills      = request.POST.get('skills', ''),
            hobbies     = request.POST.get('hobbies', ''),
            biotag      = request.POST.get('biotag', ''),
            ec_name     = request.POST.get('ec_name', ''),
            ec_relation = request.POST.get('ec_relation', ''),
            ec_phone    = request.POST.get('ec_phone', ''),
            ec_alt_phone= request.POST.get('ec_alt_phone', ''),
        )
        if request.FILES.get('photo'):
            file = request.FILES['photo']
            upload = cloudinary.uploader.upload(file, folder='employee_photos')
            emp.photo = upload['secure_url']
        emp.save()
        messages.success(request, f'Employee {emp.first_name} added successfully!')
        return redirect('employee_dashboard', pk=emp.pk)

    return render(request, 'employees/add_employee.html')
