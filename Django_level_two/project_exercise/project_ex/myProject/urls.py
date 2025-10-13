from django.urls import path
from myProject import views

urlpatterns = [
    path('',views.user,name = 'user'),
  
]