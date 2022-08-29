from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# CONNECTING TEMPLATES
def simple_view(request):
  return render(request, 'first_app/example.html') #render(request, 'templatename')

#############################################################
# articles = {
#   'sports': 'Sports Page',
#   'finance': 'Finance Page',
#   'politics': 'Politics Page'
# }

# def sports_page(request):
#   return HttpResponse(articles['sports'])

# def finance_news(request):
#   return HttpResponse(articles['finance'])

# def simple_view(request):
#   return HttpResponse("SIMPLE VIEW") 

# def news_view(request, topic):
#   return HttpResponse(articles[topic])

# def news_view(request, topic):
#   try:
#     result = articles[topic]
#     return HttpResponse(result)
#   except:
#     result = f'no page found for {topic} topic'
#     raise Http404(result) # --> later on we can add 404 html template

# REDIRECTING
# domain.com/first_app/0 ---> domain.com/first_app/finance

# def num_page_view(request, num_page):
#   topics_list = list(articles.keys())
#   topic = topics_list[num_page]
#   #result = articles[topic]

# REDIRECTING USING THE 'reverse' METHOD
#   webpage = reverse('topic-page', args=[topic]) #reverse(name, args[])
#   return HttpResponseRedirect(webpage)
  


# def add_view(request, num1, num2):
#   add_result = num1 + num2
#   result = f'{num1} + {num2} = {add_result}'
#   return HttpResponse(str(result))