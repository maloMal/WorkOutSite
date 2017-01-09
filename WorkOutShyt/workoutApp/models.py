from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
	name = models.CharField(max_length = 150)
	points = models.IntegerField(default=1)
	user = models.ManyToManyField(UserProfile)
	picture = models.ImageField(upload_to='')
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name', )

#def 


class UserProfile(models.Model):
	username = models.CharField(max_length=36, unique=True)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.username
	
	#Placeholder
	#facebookProfile = models.OneToOneField(FBProfileManager)
