from django.shortcuts import render
from django.config import settings

def index(request):
    context ={
        "restaurant_name":"My Restaurant",
        "restaurant_phone":settings.RESTAURANT_PHONE_NUMBER
    }
    return render(request,'index.html',context)