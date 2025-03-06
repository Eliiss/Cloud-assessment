from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request, 'store/Homepage.html')
def loginpage_view(request):
    return render(request, 'store/Loginpage.html')
