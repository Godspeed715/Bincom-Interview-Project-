from django.db import models

# Create your models here.
class Video(models.Model):
    page_no = models.IntegerField()
    title = models.CharField(max_length=100)
    src = models.URLField()