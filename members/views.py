from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View



def login_user(request):                # Funkcja logowania
    if request.method == "GET":
        return redirect('login')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = login(request, username, password)
        if user is not None:
            return redirect('login')
        else:
            return redirect('all_view')
    else:
        return redirect('all_view')


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('all_view')


def logout_user(request):           # Wyloguj
    logout(request)
    return redirect('all_view')


