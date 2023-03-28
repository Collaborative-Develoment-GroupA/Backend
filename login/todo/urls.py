from django.conf.urls import url
from . import views
from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,
urlpatterns = [
    url('', views.UserCreate.as_view(), name='account-create'),
    path('login/',views.LoginView),
    path('api/', include('admin.site.urls')),  
    path('userCheck/', views.userCheck),
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
]