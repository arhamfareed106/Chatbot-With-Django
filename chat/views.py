from django.shortcuts import render, redirect
from django.conf import settings

client = OpenAI(api_key='')

# Create your views here.
def index(request):
    return render(request, 'index.html')














