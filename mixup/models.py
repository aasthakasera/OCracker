from django.db import models
# from django.contrib.gis.db import models

# Create your models here.

class User(models.Model):
	restaurant_name = models.TextField(max_length=30)
	item 			= models.TextField()
	price 			= models.TextField(max_length=20)
	
    # address 		= models.CharField()
    # city 			= models.CharField(max_length=50)
