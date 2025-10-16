from django.urls import path
from myApp import views

# TEMPLATE TAGGING
app_name = 'myApp'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]