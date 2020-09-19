from django.shortcuts import render, redirect

# Create your views here.
def HomeView(request):

    print("Am I here")

    return render(request, "home/home.html")