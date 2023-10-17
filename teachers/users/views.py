from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Students, Teachers, Certificate
from .forms import CertificateForm
# Create your views here.

def students(request):
    std_list = Students.objects.all()
    teach_list = Teachers.objects.all()
    return render(request ,'index.html', {'students' : std_list, 'teachers' : teach_list})

def get_associated_teachers(request, std_id):
    try:
        std = Students.objects.get(id=std_id)
        teachers = std.teacher.all()
        teacher_data = [{'name' : teacher.name} for teacher in teachers]
        return JsonResponse({'teachers' : teacher_data})
    except Students.DoesNotExist:
        return JsonResponse({'error' : 'Student not found'}, status=404)
    
def get_associated_students(request, teacher_id):
    try:
        teach = Teachers.objects.get(pk=teacher_id)
        students = teach.students.all()
        std_data = [{'name' : student.name} for student in students]
        return JsonResponse({'students' : std_data})
    except Teachers.DoesNotExist:
        return JsonResponse({'error' : 'Teacher not found'}, status=404)
    

def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            teacher = form.cleaned_data['teacher']
            description = form.cleaned_data['description']
            certificate = Certificate(student=student, teacher=teacher, description=description)
            certificate.save()
            return redirect('view_certificate', certificate_id=certificate.pk)
    else:
        form = CertificateForm()
        
    return render(request, 'components/generate_certificate.html', {'form' : form})
    
def view_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, pk=certificate_id)
    return render(request, 'components/view_certificate.html', {'certificate': certificate})
            