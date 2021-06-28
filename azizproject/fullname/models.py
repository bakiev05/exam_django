from django.db import models


class Profile(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=100)
	birth_date = models.DateField()
	is_worker = models.BooleanField(default=True)

    
	def __str__(self):
		return f"{self.first_name} -- {self.last_name}"
