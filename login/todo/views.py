from django.shortcuts import render
from .serializers import TodoSerializer, LoginSerializer
from rest_framework import viewsets      
from .models import Todo, Login          
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all()   

class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Login.objects.all()

@csrf_exempt
def userCheck(request):
    return HttpResponse("asdsads")
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        print(f'Email: {email}, Password: {password}')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            print("Login successful")

            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
