from django.db import models

class ListOfRegistration(models.Model):
    fio = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

