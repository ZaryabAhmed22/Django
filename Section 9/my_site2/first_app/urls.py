from xml.etree.ElementInclude import include
from django.urls import path
from . import views

# urlpatterns = [
#   path('simple_view', views.simple_view),
#   path('sports_view', views.sports_page),
#   path('finance_view', views.finance_news)
# ]

# CONNECTING TEMPLATES
urlpatterns = [
  path('', views.simple_view) #domain.com/first_app
]


####################################################
# urlpatterns = [
#   path('<topic>/', views.news_view, name='topic-page'),
#   path('<int:num1>/<int:num2>', views.add_view),
#   path('<int:num_page>', views.num_page_view)
# ]