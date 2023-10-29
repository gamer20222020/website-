from django.contrib import admin
from .models import Users
from .models import Place
from .models import Event

admin.site.register(Users)

admin.site.register(Place)

admin.site.register(Event)
