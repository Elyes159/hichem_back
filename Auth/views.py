from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

from Auth.models import Admin, SuperAdmin, Utilisateur
import shortuuid


@csrf_exempt
def login_employee(request) : 
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = User.objects.get(username = username)
        superAdmin = SuperAdmin.objects.filter(user = user).exists()
        admin = Admin.objects.filter(user = user).exists()
        utilisateur = Utilisateur.objects.filter(user = user).exists()
        token = shortuuid.uuid()
        if check_password(password, user.password):
                return JsonResponse({'message': 'Connexion réussie','superAdmin':superAdmin,'admin':admin,'utilisateur':utilisateur, 'token':token , 'username':username}, status=200)
        else:
                return JsonResponse({'message': 'Mot de passe incorrect', 'status': 'failed'}, status=400)
        
        