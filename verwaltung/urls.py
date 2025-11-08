from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.start, name="start" ),
    path('login/', views.login, name="login" ),

]