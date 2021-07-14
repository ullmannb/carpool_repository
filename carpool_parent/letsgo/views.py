from django.shortcuts import render, get_object_or_404
from . import models
from .forms import RoomForm, CarForm, StudentForm
from django.shortcuts import redirect
from .models import Room, Car, Student
from django.contrib.auth.decorators import login_required



# Create your views here.
def room_list(request):
    rooms = models.Room.objects.all()
    return render(request, 'letsgo/room_list.html',{'rooms': rooms})

@login_required
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            #room.teacher = request.user
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'letsgo/room_edit.html', {'form': form})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'letsgo/room_detail.html',{'room': room})

@login_required
def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('room_detail',pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'letsgo/room_edit.html', {'form': form})

def car_list(request):
    cars = models.Car.objects.all()
    students = models.Student.objects.all()
    has_student = False
    count = 0
    car_with_student_list = []
    for car in cars:
        for student in students:
            if student.student_car == car:
                has_student = True
        if has_student:
            count+=1
            car_with_student_list.append(car)
        has_student = False
    car_boolean_student = [False]*count
    return render(request, 'letsgo/car_list.html',{'cars': cars, 'students':students, 'has_student': has_student, 'car_with_student_list':car_with_student_list, 'car_boolean_student': car_boolean_student})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'letsgo/car_detail.html',{'car': car})

@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail',pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'letsgo/car_edit.html', {'form': form})

@login_required
def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            #room.teacher = request.user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'letsgo/car_edit.html', {'form': form})

def student_list(request):
    students = models.Student.objects.all()
    rooms = models.Room.objects.all()
    has_student = False
    count = 0
    room_with_student_list = []
    for room in rooms:
        for student in students:
            if student.student_room == room:
                has_student = True
        if has_student == True:
            count += 1
            room_with_student_list.append(room)
        has_student = False
    room_student_boolean = [False]*count
    # for room in room_with_student_list:
        
    return render(request, 'letsgo/student_list.html', {'students': students, 'rooms': rooms, 'has_student' : has_student, 'room_with_student_list': room_with_student_list, 'room_student_boolean':room_student_boolean})

@login_required
def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            #room.teacher = request.user
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'letsgo/student_edit.html', {'form': form})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'letsgo/student_detail.html',{'student': student})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail',pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'letsgo/student_edit.html', {'form': form})

@login_required
def car_remove(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method =="POST":
        car.delete()
        return redirect('car_list')
    
    return render(request, "letsgo/car_remove.html")

@login_required
def student_remove(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method =="POST":
        student.delete()
        return redirect('student_list')

    return render(request, "letsgo/student_remove.html")

@login_required
def room_remove(request, pk):
    
    room = get_object_or_404(Room, pk=pk)

    if request.method == "POST":
        room.delete()
        return redirect('room_list')

    return render(request, "letsgo/room_remove.html")

def home(request):
    return render(request, "letsgo/home.html")
