from django.shortcuts import render
from .models import Event # reference the class in omdels.py
from django.http import HttpResponseRedirect
from .forms import USERform

# Create your views here.
def attendees(request):
	submitted =False 
	if request.method== "POST":
		Event_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/attendees?submitted=True')
	else:
		form = USERform
		if 'submitted' in request.GET:
			submitted=True
	return render(request,'attendees.html',{'form':form, 'submitted':submitted })
def home(request):
	return render(request,"home.html",{})

def events(request):
	event_list= Event.objects.all() #grab all from class Event
	return render(request,"events.html",{
		'events_list':event_list
		})