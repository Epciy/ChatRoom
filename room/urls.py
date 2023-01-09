
from django.urls import path
from .import views

urlpatterns =[
    path("rooms/",views.rooms,name="rooms"),
    path("createroom/",views.createroom,name="createroom"),
    path("rooms/<slug:slug>/",views.room,name="room"),
    path('rooms/<slug:slug>/delete/', views.delete_room, name='delete_room'),
  
    ]