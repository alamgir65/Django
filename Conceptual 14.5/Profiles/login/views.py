from django.shortcuts import render
from .forms import DjangoLoginForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        x = f"Name is : {name}"
        y = f"Name is : {email}"
        return render(request, 'login/home.html' , {'name': x, 'email': y})
    return render(request, 'login/home.html')

def StuForm(request):
    print(request.POST)
    return render(request, 'login/form.html')


def DjangoForm(request):
    form = DjangoLoginForm()
    
    return render(request, 'login/django_forms.html' , {'form': form })