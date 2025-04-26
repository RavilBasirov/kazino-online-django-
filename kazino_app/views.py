from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')

# def feedback(request):
#     if request.method == 'POST':
#         email_adress = request.POST.get('email')
        
#         if email_adress:
#             email = models.Email(email=email_adress, send_date=timezone.now())
#             email.save()
#             print(f"Ещё один лох имэйл кинул: {email}")
#             return JsonResponse({'status': 'success', 'message': 'Email получен'})
#         else:
#             return JsonResponse({'status': 'success', 'message': 'Email не получен'})
#     return render(request, 'feedback.html')

def auth(request):
    return render(request, 'auth.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        username = request.POST.get('login')

        user = User.objects.create_user(username, email, password)
        user.save
        login(request, user)

        print(name, login, password, email)

    return render(request, 'register.html')