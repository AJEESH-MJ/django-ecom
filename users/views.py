from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Users 
from django.contrib import messages
from django.contrib.auth import authenticate, login

def signout(request):
    logout(request)
    return redirect('home')

def show_acc(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            # create User
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Create related profile
            Users.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message = "User Registered Succesfully"
            messages.success(request, success_message)
            context['register']= False
        except Exception as e:
            error = "Duplicate username or invalid inputs"
            messages.error(request, error)
            
            return render(request, 'accounts.html', {
                'username': username,
                'email': email,
                'address': address,
                'phone': phone,
            })
    if request.POST and 'login' in request.POST:
        context['register']= False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, 'accounts.html', context)