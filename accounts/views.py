from urllib import response

from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import RegisterForm

def registration(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/home")
    else:
        form = RegisterForm()


    return render(response, "registration/registration.html", {"form":form})