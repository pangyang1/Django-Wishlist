from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages

def index(request):
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        add_user = User.objects.add_user(request.POST)

        for key, error in add_user.iteritems():
            messages.error(request, error)
        return redirect('login:index')

def login(request):
    if request.method == 'POST':
        check_user = User.objects.check_user(request.POST)
    if type(check_user) is 'dict':
        for key, error in check_user.iteritems():
            messages.error(request, error)
        return redirect('login:index')
    else:
        request.session['user_id'] = check_user
        return redirect('wish:dashboard')

# Create your views here.
