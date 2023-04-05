from django.urls import path
from . import views
from .views import AccidentList, Officerdetails

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('officer/',views.AddOfficer, name='addofficer'),
    path('accident/', views.AddAccident, name= 'accident'),
    path('accidents/', AccidentList.as_view(), name='accident-details'),
    path('officers/', Officerdetails.as_view(), name='officer-details')
]