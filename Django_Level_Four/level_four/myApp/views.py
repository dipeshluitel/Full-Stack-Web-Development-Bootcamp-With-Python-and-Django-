from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myApp/index.html')

def other(request):
    return render(request,'myApp/other.html')

def relative(request):
    return render(request,'myApp/relative_url_templates.html')