from django.db import models

# Create your models here.
class Article(models.Model):
	url = models.URLField()
	headline = models.CharField(max_length=32, default='')
	date_of_publication = models.DateField()
	main_text = models.TextField()

class Disease(models.Model):
	disease_name = models.CharField(null=True,max_length=200,blank=True)

class Syndrome(models.Model):
	syndrome_name = models.CharField(null=True,max_length=200,blank=True)
	"""docstring for Report"""
class Location(models.Model):
 	name=models.CharField(max_length = 512,blank=True)
 	latitude=models.DecimalField(max_digits=24, decimal_places=20)
 	longitude=models.DecimalField(max_digits=24, decimal_places=20)	

class Report(models.Model):
 	article = models.ForeignKey(Article,on_delete=models.CASCADE)
 	disease = models.ManyToManyField(Disease,blank=True)
 	syndrome = models.ManyToManyField(Syndrome,blank=True)
 	comment = models.TextField()

class Reportevent(models.Model):
 	report_type = models.CharField(max_length=200)
 	start_date = models.DateField()
 	end_date = models.DateField()
 	number_effecet = models.IntegerField(blank=True, null=True)
 	location = models.ForeignKey(Location,models.PROTECT)
 	report = models.ForeignKey(Report,on_delete=models.CASCADE)