from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SingUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Adress"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "username"
        self.fields["username"].label = ""

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "password"
        self.fields["password1"].label = ""

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"
        self.fields["password2"].label = ""


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@mail.com"}
        ),
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Phone "}
        ),
    )

    adress = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Adress"}
        ),
    )

    state = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "State "}
        ),
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "City  "}
        ),
    )

    zipcode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Zipcode  "}
        ),
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username  "}
        ),
    )

    class Meta:
        model = Record
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "phone",
            "city",
            "state",
            "adress",
            "zipcode",
        )
