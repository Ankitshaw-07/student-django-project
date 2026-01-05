from django.shortcuts import render
from department.models import Department
from course.models import Course
from subject.models import Subject
from studentapp.models import Student
from book.models import Book
from result.models import Result

def dashboard_view(request):
    context = {
        'total_departments': Department.objects.count(),
        'total_courses': Course.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_students': Student.objects.count(),
        'total_books': Book.objects.count(),
        'total_results': Result.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)
