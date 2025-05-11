from django.shortcuts import render

def show_acc(request):
    return render(request, 'accounts.html')