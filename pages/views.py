from django.shortcuts import render,HttpResponse


# Create your views here.
def sample1(request):
    return render(request,"home.html")

def sports(request):
    return render(request,"sports.html")

def race(request):
    return render(request,"race.html")

def casino(request):
    return render(request,"casino.html")


def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def cricket(request):
    return render(request,"cricket.html")

def football(request):
    return render(request,"football.html")

def basketball(request):
    return render(request,"basketball.html")

def icehockey(request):
    return render(request,"icehockey.html")

def f1(request):
    return render(request,"f1.html")

def bike(request):
    return render(request,"bike.html")

def horse(request):
    return render(request,"horse.html")

def start(request):
    return  render(request,"start.html")

def about(request):
    return render(request,"about.html")





