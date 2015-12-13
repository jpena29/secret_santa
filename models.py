from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Information(models.Model):
	person_name = models.CharField(max_length = 50)
	person_email = models.CharField(max_length = 50)
	def __str__(self):
		return self.person_name
