from django.shortcuts import render
from django.conf import settings

def homepage_view(request):
    return render(request, 'store/Homepage.html', {'MEDIA_URL': settings.MEDIA_URL})

def store(request):
    context = {}  #add the data to pass the store html 
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)



#im not sure if we need this views because im already calling them in users 
def loginpage_view(request):
    return render(request, 'store/Loginpage.html')

def signupPage_view(request):
    return render(request, 'store/SignupPage.html')
