from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

from Auth.models import Employe
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password



@csrf_exempt
def login_employee(request) : 
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = User.objects.get(username = username)
        if check_password(password, user.password):
                return JsonResponse({'message': 'Connexion réussie', 'status': 'success'}, status=200)
        else:
                return JsonResponse({'message': 'Mot de passe incorrect', 'status': 'failed'}, status=400)
        
        