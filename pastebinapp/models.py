from django.db import models

# Create your models here.
class Pastebin(models.Model):
	name= models.CharField(max_length=30)
	textpaste = models.CharField(max_length=80)
	pasteurl = models.AutoField(primary_key=True)
	

	def __str__(self):
		return self.name
	