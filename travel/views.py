from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Kolkata'
    dest1.desc = 'City of JOY'
    dest1.price = 17

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'City of India'
    dest2.price = 57

    dest3 = Destination()
    dest3.name = 'Mumbai'
    dest3.desc = 'City of Buisness'
    dest3.price = 19

    dests = [dest1, dest2, dest3]

    return render(request, "index.html",{'dests' : dests})
