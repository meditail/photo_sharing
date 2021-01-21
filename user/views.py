from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
#Matching query does not exist try out to register a new user
class RegisterUser(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        if password == password_repeat:
            user = User.objects.get(username=email)
            if user is  None:
               User.objects.create(email, email, password)
               new_user = User.objects.get(username=email)
               login(request, new_user)

        return redirect('artwork:my-artworks')

class LoginUser(View):
    def get(self, request):
        return render(request, 'user/login.html')

    #def post(self, request):
    #    return redirect('artwork:my-artworks')

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('artwork:list')


