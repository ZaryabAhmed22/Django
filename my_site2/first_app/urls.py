from xml.etree.ElementInclude import include
from django.urls import path
from . import views

# urlpatterns = [
#   path('simple_view', views.simple_view),
#   path('sports_view', views.sports_page),
#   path('finance_view', views.finance_news)
# ]

urlpatterns = [
  path('<topic>/', views.news_view),
  path('<int:num1>/<int:num2>', views.add_view)
]