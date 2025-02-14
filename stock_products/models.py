from django.db import models


class Article(models.Model) : 
    nom = models.CharField(max_length=400 , null=False)
    description = models.CharField(max_length=1500 , null = True)
    reference = models.CharField(primary_key=True , max_length=500)
    quantite = models.IntegerField(default=0)

class Composant(models.Model) : 
    nom = models.CharField(max_length=200)
    reference = models.CharField(primary_key=True , max_length=500)
    quantite = models.IntegerField()
    article = models.ForeignKey(Article , on_delete=models.CASCADE , null = True, related_name="article")
