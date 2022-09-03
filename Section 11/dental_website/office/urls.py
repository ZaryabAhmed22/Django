from django.urls import path
from . import views

#domain.com/office ---> list all pattients
urlpatterns = [
    path('', views.list_patients, name='list_patients')
]
