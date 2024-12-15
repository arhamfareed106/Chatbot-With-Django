from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, "chat.html")


def log(request):
    return render(request, "log.html")
    



def signup(request):
    return render(request, "signup.html")