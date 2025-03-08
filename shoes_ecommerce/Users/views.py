from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Successful Sign Up!')
            return redirect('store:store')  
        else:
            messages.error(request, 'Error. Please revise the inserted data')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'store/SignupPage.html',  {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Correct Login!')
                return redirect('store:store') 
            else:
                messages.error(request, 'Incorrect user or password.')
        else:
            messages.error(request, 'Please revise the inserted data')
    else:
        form = CustomUserLoginForm()
    
    context = {'form': form}
    return render(request, 'store/Loginpage.html', {'form': form})