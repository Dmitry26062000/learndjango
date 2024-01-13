from django.shortcuts import render
from cars.models import Car
# Create your views here.
def car(request):
    n=Car.objects.all()
    con={'car':n}
    return render(request,'car.html',context=con)