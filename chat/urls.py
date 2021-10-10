from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='chat_home'),
    path('room/<int:room_number>/', views.room, name='room'),
]