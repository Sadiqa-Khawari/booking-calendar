from django.shortcuts import render, redirect
from .forms import RegisterForm 



def home(request):
    return render(request, "reservations/home.html")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")  

    else:
        form = RegisterForm() # Uusi forms
    return render(response, "reservations/register.html", {"form": form})
