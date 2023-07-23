from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    # srNo = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prepTimeInMins = models.IntegerField()
    cookTimeInMins = models.IntegerField()
    totalTimeInMins = models.IntegerField()


    def __str__(self):
        return self.title 
    

