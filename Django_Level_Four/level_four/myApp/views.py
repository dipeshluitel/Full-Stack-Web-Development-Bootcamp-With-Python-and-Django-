from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    values = {'date': datetime.now()}
    return render(request,'myApp/index.html',context=values)

def other(request):
   string =  {"django" : "the web framework for web development"}
   return render(request,'myApp/other.html',context= string)

def relative(request):
    return render(request,'myApp/relative_url_templates.html')