from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def get(request):
    value = Question.objects.get()
    return HttpResponse(value)  