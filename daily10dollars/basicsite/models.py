from django.db import models

# Create your models here.
class Gmail(models.Model):
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	
class Facebook(models.Model):
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	image=models.FileField(null=True,blank=True)
	def __str__(self):
		return self.username
	class Meta:
		verbose_name_plural = "Facebook"	