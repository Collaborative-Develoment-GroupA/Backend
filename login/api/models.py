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
    officer_id = models.IntegerField(max_length=10, null=True, blank=True)
    department = models.CharField(max_length=50)
    post = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
