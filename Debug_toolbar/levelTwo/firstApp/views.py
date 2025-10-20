from django.shortcuts import render
from firstApp.models import Topic,AccessRecord,Webpage #First Step (follow notepad)

# Create your views here.
def index(request):
    Webpages_list = AccessRecord.objects.order_by('date') #Second Step
    date_dict = {'access_records':Webpages_list} #Second Step
    # my_dict = {'insert_content':"Hello i'm from FIRSTAPP!"}
    # return render(request,'firstApp/index.html',context=my_dict)
    return render(request,'firstApp/index.html',context=date_dict)
