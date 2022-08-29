from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
blogs = {
  'sports': 'This is a sports blog',
  'finance': 'This is a finance blog',
  'crypto': 'This is a crypto blog',
  'politics': 'This is a politics blog',
  'programming': 'This is a programming blog',
}

def view_post(request, topic):
  try:
    result = blogs[topic]
    return HttpResponse(blogs[topic])
  except:
    result = f'There is no blogposts on {topic}'
    raise Http404(result)

def page_num_redirect_view(requests, page_num):
  topics_list = list(blogs.keys())
  topic = topics_list[page_num]
  webpage = reverse('topic-page', args=[topic])
  return HttpResponseRedirect(webpage)

