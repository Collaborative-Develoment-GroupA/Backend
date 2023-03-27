from django.conf.urls import url
from . import views

urlpatterns = [
    # url('', views.UserCreate.as_view(), name='account-create'),
    # path('login/',views.LoginView),
     path('api/', include('admin.site.urls')),  
    path('userCheck/', views.userCheck)
]