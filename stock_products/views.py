from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from stock_products.models import Article, Composant

# Create your views here.

@csrf_exempt
def get_articles(request):
    if request.method == "GET":
        articles = Article.objects.all()
        articles_list = list(articles.values())

        composant = Composant.objects.all()
        composant_list = list(composant.values())

        return JsonResponse({"articles": articles_list, "composant_list": composant_list}, safe=False)

