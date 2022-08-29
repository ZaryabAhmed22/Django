from django.urls import path
from . import views

#Creating paths
urlpatterns = [
  path('<int:page_num>/', views.page_num_redirect_view),
  path('<str:topic>/', views.view_post, name='topic-page'),
]