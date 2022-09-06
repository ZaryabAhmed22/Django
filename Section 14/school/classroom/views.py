from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView,DetailView, UpdateView, DeleteView
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
# Creates a model form
class TeacherCreateView(CreateView):
  # Step 1: Connect the model
  model = Teacher

  # Step 2: Fields you want to display
  fields = '__all__'
  success_url= reverse_lazy('classroom:thank_you')

  # template --> django by default searches for a template named model_form.html

####### LIST VIEW #######
# Prints all the instances of the model declared
class TeacherListView(ListView):
  # Step 1: Connect to the model
  model = Teacher

  # Default queryset
  #queryset= Teacher.objects.all()
  # Altering the QuerySet
  queryset= Teacher.objects.order_by('first_name')

  #Changing name for object_list
  context_object_name= 'teacher_list'


  # template --> django by default searches for a template named model_list.html

####### DETAIL VIEW #######
# Details of a specific instance of the declared model
class TeacherDetailVIew(DetailView):
  #RETURN ONLY ONE MODEL ENTRY REFERING TO THE PK
  # Step 1: Connect to the model
  model = Teacher #Sends a context object
  #PK --> {{teacher}}

   # template --> django by default searches for a template named model_detail.html

####### UPDATE VIEW #######
# Mix between create view and detail view
class TeacherUpdateVIew(UpdateView):
  # SHARE model_form.html -- UPDATES dingle PK
  model = Teacher

  # fields to be updated
  fields = ['last_name', 'subject']

  #success url
  success_url= reverse_lazy('classroom:teacher_list')

####### DELETE VIEW #######
# Sends Back a form with single Delete Button
class TeacherDeleteView(DeleteView):
  model = Teacher

  #success url
  success_url= reverse_lazy('classroom:teacher_list')

  # template --> django by default searches for a template named model_confirm_delete.html