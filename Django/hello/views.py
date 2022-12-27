from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Create an index func that renders html page
def index(request):
    #return the render function that can take in the template and a placeholder as a python dict
    return render(request, "hello/index.html")

#Create a view that says hello, Abdul
def Abdul(request):
    return HttpResponse("Hello, Abdul")

#Create a view thats says hello to a string entered in the url
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
