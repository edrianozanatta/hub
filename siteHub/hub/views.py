from django.shortcuts import render
from .models import *


def home(request):
    save = "no"
    if request.method == "POST":
        email = request.POST.get('email', None)
        if email != None and email != "":
            if Email.objects.filter(email=email):
                save = "exist"
            else:
                newEmail = Email()
                newEmail.email = email
                newEmail.save()
                save = "yes"
        else:
            save = "incorret"
    return render(request, 'home.html', {'save': save})


