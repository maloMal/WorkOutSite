from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExercisesDone(models.Model):
	exercise = models.CharField(max_length = 150)


	def __str__(self):
		return self.exercise

#def 


class UserProfile(models.Model):
	username = models.CharField(max_length=36, unique=True)
	email = models.EmailField(unique=True)
	execisesDone = models.ManyToManyField(ExercisesDone)
	#Placeholder
	#facebookProfile = models.OneToOneField(FBProfileManager)
