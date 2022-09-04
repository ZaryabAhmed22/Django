from pydoc import visiblename
from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('rental_review/', view=views.rental_review, name='rental_review'),
    path('thank_you/', view=views.thank_you, name='thank_you')
]
