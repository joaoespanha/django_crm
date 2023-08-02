from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
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

    return render(request, "home.html", {"records": records})


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


def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
    return render(request, "record.html", {"customer_record": record})


def delete_record(request, pk):
    if request.user.is_authenticated:
        record_to_delete = Record.objects.get(id=pk)
        record_to_delete.delete()
        messages.success(request, "You have successfully deleted a record")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to delete a record")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully added a record")
                return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in to add a record")
        return redirect("home")


def update_record(request, pk):
    ...
