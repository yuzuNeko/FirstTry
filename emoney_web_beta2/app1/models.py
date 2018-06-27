from django.db import models

# Create your models here.
class data1(models.Model):
	first=models.CharField(max_length=30)
	second=models.CharField(max_length=20)

	class Meta:
		db_table='data1'