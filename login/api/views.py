import random
from django.conf import settings
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 

from .models import *
# from api.models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import authenticate
from django.core.mail import send_mail
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes

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
        
def AddOfficer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        citizenship = data.get('citizenship')
        department = data.get('department')
        post = data.get('post')

        if firstname and lastname and citizenship and department and post:
            existing_officer = Officer.objects.filter(
                firstname=firstname,
                lastname=lastname,
                citizenship=citizenship,
                department=department,
                post=post
            ).exists()

            if existing_officer:
                return JsonResponse({'success': False, 'message': 'Officer already exists'})
            else:
                officer = Officer.objects.create(
                    firstname=firstname,
                    lastname=lastname,
                    citizenship=citizenship,
                    department=department,
                    post=post
                )
                return JsonResponse({'success': True, 'message': 'Officer added successfully'})
        else:
            missing_fields = []
            if not firstname:
                missing_fields.append('firstname')
            if not lastname:
                missing_fields.append('lastname')
            if not citizenship:
                missing_fields.append('citizenship')
            if not department:
                missing_fields.append('department')
            if not post:
                missing_fields.append('post')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


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
        data = json.loads(request.body)
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

        if (
            city and district and date and time and fault_vehicle_number and
            fault_driver_name and fault_driver_email and fault_driver_phone and
            fault_driver_address and victim_vehicle_number and victim_name and
            victim_email and victim_phone and victim_address and injuries and description
        ):
            existing_accident = Accident.objects.filter(
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
            ).exists()

            if existing_accident:
                return JsonResponse({'success': False, 'message': 'Accident already exists'})
            else:
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
                return JsonResponse({'success': True, 'message': 'Accident added successfully'})
        else:
            missing_fields = []
            if not city:
                missing_fields.append('city')
            if not district:
                missing_fields.append('district')
            if not date:
                missing_fields.append('date')
            if not time:
                missing_fields.append('time')
            if not fault_vehicle_number:
                missing_fields.append('fault_vehicle_number')
            if not fault_driver_name:
                missing_fields.append('fault_driver_name')
            if not fault_driver_email:
                missing_fields.append('fault_driver_email')
            if not fault_driver_phone:
                missing_fields.append('fault_driver_phone')
            if not fault_driver_address:
                missing_fields.append('fault_driver_address')
            if not victim_vehicle_number:
                missing_fields.append('victim_vehicle_number')
            if not victim_name:
                missing_fields.append('victim_name')
            if not victim_email:
                missing_fields.append('victim_email')
            if not victim_phone:
                missing_fields.append('victim_phone')
            if not victim_phone:
                missing_fields.append('victim_phone')
            if not victim_address:
                missing_fields.append('victim_address')
            if not injuries:
                missing_fields.append('injuries')
            if not description:
                missing_fields.append('description')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

class AccidentList(generics.ListCreateAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer

@csrf_exempt
def AddTicket(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ticket_type = data.get('ticket_type')
        vehicle_number = data.get('vehicle_number')
        name = data.get('name')
        email = data.get('email')
        contact_number = data.get('contact_number')
        address = data.get('address')
        city = data.get('city')
        district = data.get('district')
        date = data.get('date')
        time = data.get('time')

        if ticket_type and vehicle_number and name and email and contact_number and address and city and district and date and time:
            if Ticket.objects.filter(vehicle_number=vehicle_number).exists():
                return JsonResponse({'success': False, 'message': 'Ticket with the same vehicle number already exists'})

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
            return JsonResponse({'success': True, 'message': 'Ticket added successfully'})
        else:
            missing_fields = []
            if not ticket_type:
                missing_fields.append('ticket_type')
            if not vehicle_number:
                missing_fields.append('vehicle_number')
            if not name:
                missing_fields.append('name')
            if not email:
                missing_fields.append('email')
            if not contact_number:
                missing_fields.append('contact_number')
            if not address:
                missing_fields.append('address')
            if not city:
                missing_fields.append('city')
            if not district:
                missing_fields.append('district')
            if not date:
                missing_fields.append('date')
            if not time:
                missing_fields.append('time')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


class ShowTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

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
            response_data = {'otp': otp, 'success': 'otp accquired'}
            return JsonResponse(response_data)

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
            response_data = {
                'name': user.fullName,
                'email': user.email,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    

@csrf_exempt
def customauthenticate2(email,password):
        print("Inside customauthenticate")
        print(f'Email: {email}, Password: {password}')
        try:
            data=TmsUser.objects.get(email=email,password=password)
            print('from userdb',data)
            return data
        except:
            return None

@csrf_exempt
def signup(request):
    print("Inside signup")
    if request.method == 'POST':
        data = json.loads(request.body)
        fullname = data.get('fullName')
        licenseno = data.get('licenseno')
        email = data.get('email')
        password = data.get('password')

        if fullname and licenseno and email and password:
            # Check if a user with the same email already exists
            if TmsUser.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'User with the same email already exists'})

            user = TmsUser.objects.create(
                fullName=fullname,
                licenseno=licenseno,
                email=email,
                password=password
            )
            user.save()
            return JsonResponse({'success': True, 'message': 'User created successfully'})
        else:
            missing_fields = []
            if not fullname:
                missing_fields.append('fullName')
            if not licenseno:
                missing_fields.append('licenseno')
            if not email:
                missing_fields.append('email')
            if not password:
                missing_fields.append('password')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


@csrf_exempt
def change_adminpass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('newpass')
        email = data.get('email')
        print(email)
        print(password)
        if (admin_login.objects.filter(email=email).exists()):
            data = admin_login.objects.get(email=email)
            data.password = password
            data.save()
            return JsonResponse({'success': True, 'message': 'Password changed successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Not changed'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid Request'})

@csrf_exempt
def finePay(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        fiscal_year = data.get('fiscal_year')
        province = data.get('province')
        district = data.get('district')
        chit_number = data.get('chit_number')

        if fiscal_year and province and district and chit_number:
            existing_fine = Fine.objects.filter(fiscal_year=fiscal_year, province=province, district=district, chit_number=chit_number).exists()
            if existing_fine:
                return JsonResponse({'success': False, 'message': 'Fine already exists'})
            else:
                fine = Fine.objects.create(
                    fiscal_year=fiscal_year,
                    province=province,
                    district=district,
                    chit_number=chit_number
                )
                fine.save()
                return JsonResponse({'success': True, 'message': 'Fine added successfully'})
        else:
            missing_fields = []
            if not fiscal_year:
                missing_fields.append('fiscal_year')
            if not province:
                missing_fields.append('province')
            if not district:
                missing_fields.append('district')
            if not chit_number:
                missing_fields.append('chit_number')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

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

        if vehicle_no and vehicle_type and lot_no and symbol and district_code and province:
            existing_bluebook = BluebookRenew.objects.filter(
                vehicle_no=vehicle_no,
                vehicle_type=vehicle_type,
                lot_no=lot_no,
                symbol=symbol,
                district_code=district_code,
                province=province
            ).exists()
            if existing_bluebook:
                return JsonResponse({'success': False, 'message': 'Bluebook already exists'})
            else:
                bluebook = BluebookRenew.objects.create(
                    vehicle_no=vehicle_no,
                    vehicle_type=vehicle_type,
                    lot_no=lot_no,
                    symbol=symbol,
                    district_code=district_code,
                    province=province   
                )
                bluebook.save()
                return JsonResponse({'success': True, 'message': 'Bluebook added successfully'})
        else:
            missing_fields = []
            if not vehicle_no:
                missing_fields.append('vehicle_no')
            if not vehicle_type:
                missing_fields.append('vehicle_type')
            if not lot_no:
                missing_fields.append('lot_no')
            if not symbol:
                missing_fields.append('symbol')
            if not district_code:
                missing_fields.append('district_code')
            if not province:
                missing_fields.append('province')

            missing_fields_str = ', '.join(missing_fields)
            return JsonResponse({'success': False, 'message': f'Missing data in fields: {missing_fields_str}'})
    else:
        return JsonResponse({'success': False ,'message': 'Invalid request method'})

    
class ShowBluebook(generics.ListCreateAPIView):
    queryset = BluebookRenew.objects.all()
    serializer_class = BluebookSerializer

from django.contrib.auth.decorators import login_required
# from api.models import User
@login_required
@csrf_exempt
def user_profile_api(request):
    user = request.TmsUser

    user_details = {
        'email': user.email,
        'fullName': user.fullName,
        'licenseno': user.licenseno,
    }
    return JsonResponse(user_details)