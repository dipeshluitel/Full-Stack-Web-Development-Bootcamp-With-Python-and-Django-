from django.urls import path
from myForm import views

urlpatterns = [
    path("", views.formInput, name="form"),
]
