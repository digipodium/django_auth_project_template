from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == 'GET': # agar page open kia aapne
        return render(request, 'registration/register.html',{'form':CustomUserCreationForm})
    elif request.method == 'POST': # agar form submit kra to
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)      
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()             # save the user detail in database
            login(request, user)    # let the autologin work
            return redirect(reverse('dashboard'))      # redirect to dashboard pasword
        else:
            return render(request, 'registration/register.html',{'form':CustomUserCreationForm})
