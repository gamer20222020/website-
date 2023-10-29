from django.db import models

# Create your models here.
from django.db import models
# this class is used to set up your database 
# in django,
# my username for admin is albert2020

# this class basically creates and event and have the components to the even 
#**** remember that after creating a class, aka a db table you have to push it to 
#the data base by using python3 manage.py make a migration and push migration 
# django use this class and converted into database language for us 


class Place(models.Model):
	name=models.CharField('place',max_length=120)
	address=models.CharField('address',max_length=300)
	zip_code=models.CharField(' zip code',max_length=10)
	phone=models.CharField('contact',max_length=120)
	email=models.EmailField('email')
	def __str__(self):
		return self.name

class Users(models.Model):
	first_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)

	def __str__(self):
		return self.first_name


class Event(models.Model):
	name=models.CharField('Event name', max_length=120)
	event_date=models.DateTimeField('Event data ')                  #on delete is if you delete events, places are deleted too from the other db
	manager=models.CharField(max_length=60)
	place =models.ForeignKey(Place,blank=True, null=True,on_delete=models.CASCADE)# allows us to connect 2 tables 
	description=models.TextField(blank=True)# let you skip this field
	attendies=models.ManyToManyField(Users) # we want users to be able to go to many event 
	

	def __str__(self):
		return self.name#this to have the event name
	# on the admin area
