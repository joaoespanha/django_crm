from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
