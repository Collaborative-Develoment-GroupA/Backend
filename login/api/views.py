from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


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

# @api_view(['GET'])
# def officerdetails(request):
#     officers=Officer.objects.all()
#     serializer=officerdetailserializer(officers,many=True)
#     return Response(serializer.data)
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
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # def get(self, request):
        # accidents = Accident.objects.all()
        # serializer = AccidentSerializer(accidents, many=True)
        # return Response(serializer.data)
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer

def auth(request):
    if request.method==POST:
        if simon.loggedin():
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')

# def login(request):
#     if request.method==POST:
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('dashboard')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request,'login.html') 

# def logout(request):   
#     auth.logout(request)
#     return redirect('login')