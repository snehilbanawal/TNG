from email.policy import default
from django.db import models

class cashbackus(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField(default=0)
    amount= models.CharField(max_length=50)
    
    # services = models.CharField(max_length=50, choices=service_category)
    def __str__(self):
        return self.name


