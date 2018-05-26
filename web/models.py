from django.db import models

# Create your models here.
class Plate(models.Model):
	name = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='plate')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)