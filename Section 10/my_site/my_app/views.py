from django.shortcuts import render

# Create your views here.
def example_view(request):
  #my_app/templates/my_app/exampl.html
  return render(request, 'my_app/example.html')

def variable_view(request):

  my_var = {
    'first_name': 'Rosalind',
    'last_name': 'Franklin',
    'some_list': [1,2,3],
    'some_dict': {'inside_key': 'key123'},
    'user_logged_in': True,
    'pro_subs': False,
    'courses': 5,
  }


  return render(request, 'my_app/variable.html', context=my_var)

def extended_view(request):
  return render(request, 'my_app/extended.html')