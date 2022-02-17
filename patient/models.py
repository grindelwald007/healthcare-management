from django.db import models
from doctor import models as doctor_models


# Create your models here.

class PATIENT(models.Model):
    MALE = 'ml'
    FEMALE = 'fl'
    NON_BINARY = 'nb'
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Others')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICE
    )
    email = models.EmailField(null=True)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class PAYMENT(models.Model):
    CASH = 'CSH'
    BKASH = 'BKS'
    ROCKET = 'RKT'
    CARD = 'CRD'
    NAGAD = 'NGD'
    PAYMENT_CHOICE = [
        (CASH, 'Cash'),
        (BKASH, 'Bkash'),
        (NAGAD, 'Nagad'),
        (ROCKET, 'Rocket'),
        (CARD, 'Card')
    ]
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    method = models.CharField(
        max_length=3,
        choices=PAYMENT_CHOICE
    )

    def __str__(self):
        return 'id ' + str(self.id) + ' .amount = ' + str(self.amount)


class APPOINTMENT(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(PATIENT, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor_models.DOCTOR, on_delete=models.CASCADE)
    payment = models.ForeignKey(PAYMENT, on_delete=models.CASCADE)

    def __str__(self):
        return 'Patient ID = ' + str(self.patient) + ' Doctor ID = ' + str(self.doctor)
