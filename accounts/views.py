from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model  ,login, logout, authenticate
from django.contrib import messages



def signup(request):
    User = get_user_model()
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            error_message = 'Le compte utilisateur existe déjà.'
        else:
          

            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/signup.html', {'error_message': error_message})

def logout_user(request):
    logout(request)
    return redirect('index')



def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'accounts/login.html')
