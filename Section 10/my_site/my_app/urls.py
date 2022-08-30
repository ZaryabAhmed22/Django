from django.urls import path
from . import views

urlpatterns = [
  path('variable/', views.variable_view),
  path('example/', views.example_view)
  ]