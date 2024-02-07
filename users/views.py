from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    return render(request, 'users/user_create.html')