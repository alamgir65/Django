from django.shortcuts import render,redirect
from .forms import ProfileForm
# Create your views here.

def add_profiles(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = ProfileForm()
    return render(request, 'profiles/add_profile.html' , {'profile_form': profile_form})
