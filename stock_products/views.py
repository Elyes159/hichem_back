import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from stock_products.models import Article, Composant
from django.shortcuts import get_object_or_404

@csrf_exempt
def get_articles(request):
    if request.method == "GET":
        articles = Article.objects.all()
        articles_list = list(articles.values())
        composant = Composant.objects.all()
        composant_list = list(composant.values())
        return JsonResponse({"articles": articles_list, "composant_list": composant_list}, safe=False)

@csrf_exempt
def update_quantite(request) : 
    if request.method == "POST" : 
        data = json.loads(request.body)
        quantite = data.get("quantite")
        reference_article = data.get("reference_article")
        article = get_object_or_404(Article, reference =reference_article)
        article.quantite = quantite
        article.save()
        return JsonResponse({"success": "modifié"}, safe=False , status = 200)
    
@csrf_exempt
def update_quantiteC(request) : 
    if request.method == "POST" : 
        data = json.loads(request.body)
        quantite = data.get("quantite")
        reference_c = data.get("reference_c")
        composant = get_object_or_404(Composant, reference =reference_c)
        composant.quantite = quantite
        composant.save()
        return JsonResponse({"success": "modifié"}, safe=False , status = 200)
 
@csrf_exempt
def get_composant(request):
    if request.method == "POST":
        data = json.loads(request.body)
        reference = data.get("reference")
        composants = Composant.objects.filter(article__reference=reference)
        composants_list = list(composants.values())
        
        return JsonResponse({"composants": composants_list,} , status = 200)
        
        
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_article(request): 
    if request.method == "POST": 
        try:
            data = json.loads(request.body)

            reference = data.get("reference")
            description = data.get("description")
            quantite = data.get("quantite")

            if not all([reference, description, quantite]):
                return JsonResponse({"error": "Tous les champs sont requis"}, status=400)

            article = Article.objects.create(
                reference=reference,
                description=description,
                quantite=quantite
            )
            article.save()

            return JsonResponse({
                "message": "Article ajouté avec succès",
                
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)



@csrf_exempt
def add_composant(request): 
    if request.method == "POST": 
        try:
            data = json.loads(request.body)
            referenceA = data.get("referenceA")
            reference = data.get("reference")
            quantite = data.get("quantite")

            if not all([reference,referenceA, quantite]):
                return JsonResponse({"error": "Tous les champs sont requis"}, status=400)
            article = Article.objects.get(reference = referenceA)

            composant = Composant.objects.create(
                reference=reference,
                quantite=quantite,
                article = article,
            )
            composant.save()

            return JsonResponse({
                "message": "Article ajouté avec succès",
                
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données JSON invalides"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)