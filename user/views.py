from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class RegisterUser(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        if not '@' in email and len(email) < 5:
            return render(request, 'user/register.html', {'error': 'ip addresse wurde getracked und wird unmittelbar weiter gegben'})

        

        if User.objects.filter(username=email).exists():
            return render(request, 'user/register.html', {'error': 'Email exisitiert bereits.'})
        elif len(password) < 5:
            return render(request, 'user/register.html', {'error': 'Passwort muss mindestens 5 Zeichen haben.'})
        elif not password == password_repeat:
            return render(request, 'user/register.html', {'error': 'Passwort stimmt nicht überein.'})

        User.objects.create_user(email, email, password)
        user = authenticate(username=email, password=password)
        login(request, user)

        return redirect('artwork:my-artworks')

class LoginUser(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            return render(request, 'user/login.html', {'error': 'Username oder Passwort sind falsch.'})

        login(request, user)
        return redirect('artwork:my-artworks')

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('artwork:list')


