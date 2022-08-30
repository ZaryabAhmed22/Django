from django.urls import path
from . import views

# register the app namespace
# used in URL names
app_name = 'my_app'

urlpatterns = [
  path('extended/', views.extended_view, name='extended'),
  path('variable/', views.variable_view, name='variable'),
  path('example/', views.example_view, name='example'),
  ]

