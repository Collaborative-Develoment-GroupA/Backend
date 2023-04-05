from django.db import models


class admin_login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.email

class Officer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    citizenship= models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    post = models.CharField(max_length=50)

class Accident(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    fault_vehicle_number = models.CharField(max_length=100)
    fault_driver_name = models.CharField(max_length=100)
    fault_driver_email = models.EmailField()
    fault_driver_phone = models.CharField(max_length=100)
    fault_driver_address = models.TextField()
    victim_vehicle_number = models.CharField(max_length=100)
    victim_name = models.CharField(max_length=100)
    victim_email = models.EmailField()
    victim_phone = models.CharField(max_length=100)
    victim_address = models.TextField()
    injuries = models.TextField()
    description = models.TextField()

