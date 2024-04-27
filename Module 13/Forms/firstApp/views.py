from django.shortcuts import render
from . forms import contactForm, StudentForm , passwordValidationProject
# Create your views here.

def home(request):
    return render(request, 'firstApp/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'firstApp/about.html', {'name':name, 'email':email, 'select': select })
    else: return render(request, 'firstApp/about.html')

def form(request):
    return render(request, 'firstApp/form.html')

def DjangoForm(request):
    if request.method == 'POST':
        Form = contactForm(request.POST, request.FILES )
        if Form.is_valid():
            # how to file upload in django  
            # file = Form.cleaned_data['file']
            # with open('firstApp/upload/' + file.name , 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(Form.cleaned_data)
    else:
        Form = contactForm()
    return render(request, 'firstApp/django_form.html', {'form' : Form})



def Student_form(request):
    if request.method == 'POST':
        Form = StudentForm(request.POST, request.FILES)
        if Form.is_valid():
            print(Form.cleaned_data)
    else:
        Form = StudentForm()
    return render(request, 'firstApp/Django_form.html/' , {'form': Form})



def passworsValidation(request):
    
    if request.method == 'POST':
        form = passwordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()
    return render(request, 'firstApp/Django_form.html/' , {'form': form})