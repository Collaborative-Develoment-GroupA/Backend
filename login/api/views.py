from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 

from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

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
        # officer_id = data.get('id')
        department = data.get('department')
        post = data.get('post')

        officer = Officer.objects.create(
            firstname=firstname,
            lastname=lastname,
            citizenship=citizenship,
            # officer_id=id,
            department=department,
            post=post
        )
        officer.save()


        return JsonResponse({'success': True ,'message': 'Officer added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})

class Officerdetails(generics.ListCreateAPIView):
    queryset = Officer.objects.all()
    serializer_class = Officerdetailserializer

@csrf_exempt
def AddAccident(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        city = data.get('city')
        district = data.get('district')
        date = data.get('date')
        time = data.get('time')
        fault_vehicle_number = data.get('fault_vehicle_number')
        fault_driver_name = data.get('fault_driver_name')
        fault_driver_email = data.get('fault_driver_email')
        fault_driver_phone = data.get('fault_driver_phone')
        fault_driver_address = data.get('fault_driver_address')
        victim_vehicle_number = data.get('victim_vehicle_number')
        victim_name = data.get('victim_name')
        victim_email = data.get('victim_email')
        victim_phone = data.get('victim_phone')
        victim_address = data.get('victim_address')
        injuries = data.get('injuries')
        description = data.get('description')

        accident = Accident.objects.create(
            city=city,
            district=district,
            date=date,
            time=time,
            fault_vehicle_number=fault_vehicle_number,
            fault_driver_name=fault_driver_name,
            fault_driver_email=fault_driver_email,
            fault_driver_phone=fault_driver_phone,
            fault_driver_address=fault_driver_address,
            victim_vehicle_number=victim_vehicle_number,
            victim_name=victim_name,
            victim_email=victim_email,
            victim_phone=victim_phone,
            victim_address=victim_address,
            injuries=injuries,
            description=description
        )
        accident.save()


        return JsonResponse({'success': True ,'message': 'Accident added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})

class AccidentList(generics.ListCreateAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer

@csrf_exempt
def AddTicket(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        ticket_type= data.get('ticket_type')
        vehicle_number = data.get('vehicle_number')
        name = data.get('name')
        email = data.get('email')
        contact_number= data.get('contact_number')
        address = data.get('address')
        city= data.get('city')
        district= data.get('district')
        date = data.get('date')
        time = data.get('time')
    
        ticket = Ticket.objects.create(
            ticket_type=ticket_type,
            vehicle_number=vehicle_number,
            name=name,
            email=email,
            contact_number=contact_number,
            address=address,
            city=city,
            district=district,
            date=date,
            time=time
        )
        ticket.save()
        return JsonResponse({'success': True ,'message': 'Ticket added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})

class ShowTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
