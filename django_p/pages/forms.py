from django import forms
from django.forms import ModelForm 
# why model because it  adds data to the database 
from .models import Users 
# i want to add more attendees 


#create a form 

class USERform(ModelForm):
	class Meta:
		model =Users
		fields=('first_name','last_name')
		
			