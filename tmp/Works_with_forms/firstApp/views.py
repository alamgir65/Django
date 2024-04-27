from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'firstApp/index.html')

def form(request):   
    return render(request, 'firstApp/form.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'firstApp/about.html', {'name': name, 'email': email})
    return render(request, 'firstApp/about.html')