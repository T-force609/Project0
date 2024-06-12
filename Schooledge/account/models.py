from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.

class ApplicantForm(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    firstname= models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100,  blank=False)
    lastname = models.CharField(max_length=100,  blank=False)
    gender = models.CharField(max_length=15, choices=GENDER, default='male')
    Date_of_birth = models.DateTimeField(default=timezone.now)
    cls = models.CharField(max_length=10)
    phone_number = models.IntegerField(blank=False )
    Email_Address = models.EmailField(blank=False)
    passport= models.ImageField()
    birth_certificate = models.ImageField()
    country = CountryField(blank=True, )
    state = models.CharField(max_length=100, blank=False)
    Address = models.CharField(max_length=350)

    class Mate:
        ordering = ('-date_of_birth',)

    def __str__(self):
        return self.firstname


class ParentForm(models.Model):
    Fathername = models.CharField(max_length=250, blank=False)
    Mothername = models.CharField(max_length=250, blank=False)
    F_number = models.IntegerField()
    M_number =models.IntegerField()
    F_occupation =models.CharField(max_length=15, blank=False)
    M_occupaion = models.CharField(max_length=15, blank=False)

    class Mate:
        ordering = ('-date_of_birth',)

    def __str__(self):
        return self.Fathername

    
