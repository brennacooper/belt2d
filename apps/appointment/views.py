from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Appointment
from ..loginreg.models import User
from datetime import datetime


# Create your views here.
def index(request):
	date = datetime.now().date().strftime('%B %d, %Y')
	context = {
	"appointments": Appointment.objects.all(),
    "date": date,
		
	}

	return render(request, "appointment/index.html", context)

def create(request):
	
	Appointment.objects.create(date = request.POST['date'], time=request.POST['time'], task=request.POST['task'])

	return redirect ('appointment:index')

def edit (request, id):
	context = {
		"appintment": Appointment.objects.get(id=id)
	}
	return render(request, "appointment/edit.html", context)

def delete(request, id):
	Appointment.objects.filter(id=id).delete()

	return redirect ('appointment:index')
