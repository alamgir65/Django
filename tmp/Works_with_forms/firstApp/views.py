from django.shortcuts import render , redirect
from . import models
from firstApp.forms import StudentForm
# Create your views here.

# def index(request):
#     datas = models.Student.objects.all()
#     return render(request, 'firstApp/index.html', {'datas' : datas})

# def student_delete(request,roll):
#     stu = models.Student.objects.get(pk=roll).delete()
#     return redirect('Homepage')


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'firstApp/index.html' , {'form' : form})
    
