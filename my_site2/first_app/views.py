from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

articles = {
  'sports': 'Sports Page',
  'finance': 'Finance Page',
  'politics': 'Politics Page'
}

# def sports_page(request):
#   return HttpResponse(articles['sports'])

# def finance_news(request):
#   return HttpResponse(articles['finance'])

# def simple_view(request):
#   return HttpResponse("SIMPLE VIEW") 

def news_view(request, topic):
  return HttpResponse(articles[topic])