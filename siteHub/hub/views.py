from django.shortcuts import render
from .models import *


def home(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        newEmail = Email()
        newEmail.email = email
        newEmail.save()
    return render(request, 'home.html')


