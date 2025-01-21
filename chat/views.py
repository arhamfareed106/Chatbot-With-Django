from os import remove
from django.shortcuts import render
from openai import openAPI

client = OpenAI(api_key='')

# Create your views here.
def index(request):
    return render(request, 'index.html')





















