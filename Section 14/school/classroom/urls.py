from django.urls import path
from . import views
app_name = 'classroom'

urlpatterns = [
    # path('', views.home_view, name = 'home') #path expects a function
    path('', views.HomeView.as_view(), name='home'), # CBV
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'), path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', views.TeacherDetailVIew.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>', views.TeacherUpdateVIew.as_view(), name='update_teacher')
]
