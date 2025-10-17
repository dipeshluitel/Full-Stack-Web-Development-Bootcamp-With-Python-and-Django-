from django.urls import path
from myApp import views
app_name = 'myApp'

urlpatterns = [
    path('register/',views.register,name='register'),
]