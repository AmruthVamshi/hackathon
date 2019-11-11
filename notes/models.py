from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
	title=models.CharField(max_length=300)
	body=models.TextField()
	thumb=models.ImageField(blank=True,upload_to='media/',default='default.png')
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title