from django.shortcuts import render, HttpResponse, redirect

def dashboard(request):
    return render(request, 'wish/dashboard.html')

def create(request):
    return render(request, 'wish/create.html')

def item(request):
    return render(request, 'wish/item.html')

# Create your views here.
