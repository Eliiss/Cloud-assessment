from django.shortcuts import render

def homepage_view(request):
    return render(request, 'store/Homepage.html')

def loginpage_view(request):
    return render(request, 'store/Loginpage.html')

def signupPage_view(request):
    return render(request, 'store/SignupPage.html')
