from django.shortcuts import render
from .models import Food

# Create your views here.

def food_types(request):
    foods = Food.objects.all ()
    return  render ( request,'calorie_tracker/food_type.html',{'foods': foods} )
    