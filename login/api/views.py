from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response



@csrf_exempt
def Login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(f'Email: {email}, Password: {password}')
        user = customauthenticate(email=email, password=password)
        print(user)
        if user is not None:
            print("Login successful")

            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
@csrf_exempt
def customauthenticate(email,password):
        print("Inside customauthenticate")
        print(f'Email: {email}, Password: {password}')
        try:
            data=admin_login.objects.get(email=email,password=password)
            print('from userdb',data)
            return data
        except:
            return None
@csrf_exempt
def AddOfficer(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        citizenship = data.get('citizenship')
        officer_id = data.get('id')
        department = data.get('department')
        post = data.get('post')

        officer = Officer.objects.create(
            firstname=firstname,
            lastname=lastname,
            citizenship=citizenship,
            officer_id=officer_id,
            department=department,
            post=post
        )
        officer.save()


        return JsonResponse({'success': True ,'message': 'Officer added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})