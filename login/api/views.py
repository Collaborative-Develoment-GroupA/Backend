import random
from django.conf import settings
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 

from .models import *
from api.models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import authenticate
from django.core.mail import send_mail

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
def deleteOfficer(request, id):
    if request.method == 'POST':
        officer = Officer.objects.get(id=id)
        officer.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid credentials'})


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

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes
@csrf_exempt
@renderer_classes([JSONRenderer])
def forget(request):
    print("Inside forget")
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        if email:
            otp = str(random.randint(100000, 999999))
            # Compose the email message
            subject = 'Your OTP for password reset'
            message = f'Your OTP is {otp}.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            # Send the email using Gmail
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            # Store the OTP in the session for later verification
            request.session['otp'] = otp
            request.session['email'] = email
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})

        else:
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})


    return JsonResponse({'success': True, 'message': 'Password changed successfully'})


@csrf_exempt
def UserLogin(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(f'Email: {email}, Password: {password}')
        user = customauthenticate2(email=email, password=password)
        print(user)
        if user is not None:
            print("Login successful")

            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def customauthenticate2(email,password):
        print("Inside customauthenticate")
        print(f'Email: {email}, Password: {password}')
        try:
            data=User.objects.get(email=email,password=password)
            print('from userdb',data)
            return data
        except:
            return None

@csrf_exempt
def signup(request):
    print("Inside signup")
    if request.method == 'POST':
        data=json.loads(request.body)
        fullname= data.get('fullName')
        licenseno= data.get('licenseno')
        email = data.get('email')
        password=data.get('password')

        print(email)
        try:
            data== User.objects.get(email=email)
            return JsonResponse({'success': False, 'message': 'User already exists'})
        except:
            user = User.objects.create(
                fullName=fullname,
                licenseno=licenseno,
                email=email,
                password=password
            )
            user.save()
            return JsonResponse({'success': True, 'message': 'User created successfully'})

    else:
        return Response({'message': 'Invalid request method'})
    

@csrf_exempt
def UserLogout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True, 'message': 'Logout successful'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    

# @csrf_exempt
# def UserChangePassword(request):
#     if request.method == 'POST':
#         data=json.loads(request.body)
#         email = data.get('email')
#         old_password = data.get('old_password')
#         new_password = data.get('new_password')
#         print(f'Email: {email}, Old Password: {old_password}, New Password: {new_password}')
#         user = customauthenticate(email=email, password=old_password)
#         if user is not None:
#             user.set_password(new_password)
#             user.save()
#             return JsonResponse({'success': True, 'message': 'Password changed successfully'})
#         else:
#             return JsonResponse({'success': False, 'message': 'Invalid credentials'})
#     else:
#         return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def finePay(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        fiscal_year = data.get('fiscal_year')
        province = data.get('province')
        district = data.get('district')
        chit_number = data.get('chit_number')

        fine = Fine.objects.create(
            fiscal_year = fiscal_year,
            province = province,
            district = district,
            chit_number = chit_number
        )
        fine.save()
        return JsonResponse({'success': True, 'message': 'Fine added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})

class ShowFine(generics.ListCreateAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

@csrf_exempt
def Bluebook(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        vehicle_no = data.get('vehicle_no')
        vehicle_type = data.get('vehicle_type')
        lot_no = data.get('lot_no')
        symbol = data.get('symbol')
        district_code = data.get('district_code')
        province = data.get('province')

        bluebook = Bluebook.objects.create(
            vehicle_no = vehicle_no,
            vehicle_type = vehicle_type,
            lot_no = lot_no,
            symbol = symbol,
            district_code = district_code,
            province = province
        )
        bluebook.save()
        return JsonResponse({'success': True, 'message': 'Bluebook added successfully'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})
    
class ShowBluebook(generics.ListCreateAPIView):
    queryset = Bluebook.objects.all()
    serializer_class = BluebookSerializer

