from django.db import models
from datetime import datetime 
# Create your models here.

class Car_MB(models.Model):
	car_brand = models.CharField(max_length = 250)
	car_model = models.CharField(max_length = 250)
	date_entered = models.DateTimeField (default = datetime.now)

	def __unicode__(self):
		return "%s %s" % (self.car_brand, self.car_model)



