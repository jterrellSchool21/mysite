from django.db import models

class Main(models.Model):
	main_text = models.CharField(max_length=255)
	pub_date = models.DateTimeField('date published')

class Option(models.Model):
	main = models.ForeignKey(Main, on_delete=models.CASCADE)
	text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)