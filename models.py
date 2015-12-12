from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Information(models.Model):
	person_name = models.CharField(max_length = 50)
	person_email = models.CharField(max_length = 50)

