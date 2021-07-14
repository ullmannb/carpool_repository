

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# added with user creation
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 
from datetime import date

class Room(models.Model):
    location = models.CharField(max_length=150)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True, blank = True)
    # students = models.ManyToManyField(Student)
    # exists = models.BooleanField(default = False)

    def __str__(self):
        return self.location
    
class Car(models.Model):
    identifier = models.CharField(max_length=8)
    desc = models.TextField(blank=True, null=True)
    driver = models.CharField(max_length=100)

    def __str__(self):
        return self.driver + ' in ' + self.identifier

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField(null = True, blank = True, validators=[MaxValueValidator(9)])
    student_room = models.ForeignKey(Room, on_delete=models.PROTECT)
    student_car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True, blank = True)

    def __str__(self):
        return self.student_name

#added with user creation
# class User(AbstractUser):
#     username = models.CharField(max_length = 50, blank = False, null = False, unique = False)
#     email = models.EmailField(_('email address'), unique = True)
#     native_name = models.CharField(max_length = 5)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#     def __str__(self):
#         return "{}".format(self.email)