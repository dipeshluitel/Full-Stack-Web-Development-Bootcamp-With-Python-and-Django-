from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'myApp/help.html',context=helpdict)

def index(request):
    return HttpResponse("<h1>This is home page</h1>")
 