from django.contrib import admin

from stock_products.models import Article, Composant

# Register your models here.
admin.site.register(Article)

admin.site.register(Composant)