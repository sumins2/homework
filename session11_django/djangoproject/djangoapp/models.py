from django.db import models

# Create your models here.
class text(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    category = models.TextField()
    time = models.TextField()
    