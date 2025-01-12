from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def restaurant_booking(request):
    return HttpResponse("book table")