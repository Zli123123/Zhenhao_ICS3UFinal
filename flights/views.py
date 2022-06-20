from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from django.urls import reverse


from .models import Flight, Airport, Passenger

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

# Create your views here.

'''
Views for the app 'flights' is created here. There is an index page that returns an flights/index.html with 3 
inputs (flight objects, the date, the time). Also, there is a flight views that showcases the passengers to the 
specific flight. Finally, there is a view that allows you to book or delete flights. 
'''
def index(request):
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
        "date": d1,
        "time": current_time,
    })

def flight(request, flight_id):
    over = True
    max_id = Flight.objects.last().id
    if flight_id <= max_id:
        flight = Flight.objects.get(pk=flight_id)
        return render(request, "flights/flight.html" ,{
            "flight": flight,
            "over": over,
            "passengers": flight.passengers.all(),
            "num": len(flight.passengers.all()),
            "non_passengers": Passenger.objects.exclude(flights=flight).all()
        })
    else:
        over = False
        return render(request, "flights/flight.html" ,{
            "over": over
        })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        if 'passengeradd' in request.POST:
            passenger_add = Passenger.objects.get(pk=int(request.POST["passengeradd"]))
            passenger_add.flights.add(flight)
        else:
            passenger_remove = Passenger.objects.get(pk=int(request.POST["passengerremove"]))
            passenger_remove.flights.remove(flight)

        return HttpResponseRedirect(reverse("airport:flight", args=(flight.id,)))
