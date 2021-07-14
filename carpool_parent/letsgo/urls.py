from django.urls import path
from . import views


# added with user creation
# from django.contrib import admin 
# from django.conf.urls import include

urlpatterns = [
    path('room/list/',views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/new/', views.room_new, name='room_new'),
    path('room/<int:pk>/edit/', views.room_edit,name='room_edit'),
    path('room/<pk>/remove/', views.room_remove, name='room_remove'),
    path('car/list/', views.car_list, name='car_list'),
    path('car/<int:pk>/',views.car_detail, name='car_detail'),
    path('car/<int:pk>/edit/', views.car_edit,name='car_edit'),
    path('car/new/', views.car_new, name='car_new'),
    path('car/<pk>/remove/', views.car_remove, name='car_remove'),
    path('student/list/',views.student_list, name='student_list'),
    path('student/new/', views.student_new, name='student_new'),
    path('student/<int:pk>/edit/', views.student_edit,name='student_edit'),
    path('student/<int:pk>/',views.student_detail, name='student_detail'),
    path('student/<pk>/remove/', views.student_remove, name='student_remove'),
    path('', views.home, name='home'),

    # # added with user creation
    # path('auth/', include('rest_auth.urls')),

]