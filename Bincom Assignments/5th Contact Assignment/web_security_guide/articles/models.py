from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class OwaspTop10(models.Model):
    page_no = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    prevention = models.JSONField(default=list)
    attack_scenarios =  models.JSONField(default=list)