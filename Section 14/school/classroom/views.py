from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView
from classroom.froms import ContactForm
from classroom.models import Teacher

# Create your views here.
def home_view(request):
  return render(request, 'classroom/home.html')

####### TEMPLATE VIEW #######
class HomeView(TemplateView):
  template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
  template_name= 'classroom/thank_you.html'

####### FORM VIEW #######
class ContactFormView(FormView):
  form_class = ContactForm
  template_name= 'classroom/contact.html'

  # succes URL?
  #success_url= '/classroom/thank_you' #URL 
  success_url= reverse_lazy('classroom:thank_you')

  # what to do with from?
  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

####### CREATE VIEW #######
class TeacherCreateView(CreateView):
  # Step 1: Connect the model
  model = Teacher

  # Step 2: Fields you want to display
  fields = '__all__'
  success_url= reverse_lazy('classroom:thank_you')

  # template --> django by default searches for a template named model_form.html

####### LIST VIEW #######
class TeacherListView(ListView):
  # Step 1: Connect to the model
  model = Teacher

  # template --> django by default searches for a template named model_list.html