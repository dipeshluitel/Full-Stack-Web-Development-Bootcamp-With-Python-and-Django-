from django.shortcuts import render
from myProject.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'myProject/index.html')

def user(request):
    user_list = User.objects.order_by('f_name')
    user_dict = {'users':user_list}
    return render(request,'myProject/user.html',context=user_dict)
