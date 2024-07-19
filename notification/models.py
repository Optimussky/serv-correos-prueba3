from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username


class DataSystem(models.Model):
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Notification(models.Model):
    uuid = models.ForeignKey(DataSystem, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()

    def __title__(self):
        return self.title



