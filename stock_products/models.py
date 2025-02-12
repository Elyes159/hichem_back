from django.db import models

class Article(models.Model) : 
    nom = models.CharField(max_length=400 , null=False)
    description = models.CharField(max_length=1500 , null = True)
    reference = models.CharField(primary_key=True , max_length=500)
    quantite = models.IntegerField(default=0)
    
