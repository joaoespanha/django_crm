from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm


# Create your views here.
def home(request):
    # check if user is logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in ")
        else:
            messages.success(request, "There was an error to login")
            return redirect("home")

    return render(request, "home.html", {})


def login_user(request):
    ...


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Auth and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, "You have been logged in")

            return redirect("home")
    else:
        form = SingUpForm()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})
