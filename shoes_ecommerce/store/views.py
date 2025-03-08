from django.shortcuts import render

def homepage_view(request):
    return render(request, 'store/Homepage.html')

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
