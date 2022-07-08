from django.urls import path
from . import views

urlpatterns = [path('', views.Home, name="home"),
               path('room/<str:pk>/', views.Rooms, name="room"),
               path('create-room/', views.createRoom, name="create-room"),
               path('update-room/<str:pk>', views.updateRoom, name="update-room"),
               ]
