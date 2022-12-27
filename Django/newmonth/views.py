from django.shortcuts import render

#import the date module
import datetime

# Create your views here.
def index(request):
    currentDate = datetime.datetime.now()
    now = currentDate.day
    return render(request, 'newmonth/index.html',{
        "currentDate": currentDate.date(),
        "now": now == 1,
    })