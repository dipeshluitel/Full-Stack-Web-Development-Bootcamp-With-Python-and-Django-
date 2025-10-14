from django.shortcuts import render
from django.http import HttpResponse
from myForm import forms

# Create your views here.
def index(request):
    return render(request,'myForm/index.html')

def formInput(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
           print("Validation Success")
           print("NAME: "+ form.cleaned_data['name'])
           print("EMAIL: "+ form.cleaned_data['email'])
           print("TEXT: "+ form.cleaned_data['text'])


    return render(request,'myForm/form.html', context={'form':form})