from django.db import models


# Create your models here.

class DOCTOR(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    chamber_address = models.CharField(max_length=100)
    registration_number = models.IntegerField()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)