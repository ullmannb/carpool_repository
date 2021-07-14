from django import forms
from .models import Room, Car, Student
from django.contrib.auth.forms import UserCreationForm


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('location', 'teacher',)

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('identifier', 'driver')

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('student_name', 'grade', 'student_room', 'student_car')

