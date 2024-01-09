from django.shortcuts import render
from .models import *
# Create your views here.
def contents(request):
    md=Media.objects.all()
    lst={
        'cars':['mercedes','bmw'],
    }
    s={'md':md,
       'lst':lst}
    return render(request,context=s)