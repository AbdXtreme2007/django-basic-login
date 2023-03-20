from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            user = User.objects.get(name=name, password=password)
            return render(request, 'login_success.html')
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid name or password'})
    else:
        return render(request, 'login.html')