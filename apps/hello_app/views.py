from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = { 
        "students" : [
       		{'name' : 'Michael', 'age' : 35},
       		{'name' : 'John', 'age' : 30 },
       		{'name' : 'Mark', 'age' : 25},
       		{'name' : 'KB', 'age' : 27}
    	]
    }
    return render(request, "hello_app/index.html", context)

def goodbye(request):
    return HttpResponse("Smell ya later!")

def message(request):
    print("/////////////////////////////////////")
    print("Welcome to the message route!")
    return HttpResponse("Check the terminal!")

def greet(request,my_var):
    return HttpResponse("Hello " + my_var)
