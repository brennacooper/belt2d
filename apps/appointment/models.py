from __future__ import unicode_literals


from django.db import models
from ..loginreg.models import User

# Create your models here.
class Appointment(models.Model):
	task = models.CharField(max_length=255)
	date = models.DateTimeField(null= True, blank=True)
	time =  models.DateTimeField(null= True, blank=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ManyToManyField(User, related_name="appointments")

