"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# www.examples.com/app --> exampl.com/app
#setting up automatic permanent redirect using RedirectVire CBV

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='catalog/')),
    path('accounts/', include('django.contrib.auth.urls'))
]

# The path -->  'accounts/', include('django.contrib.auth.urls') automatically creates these url paths ofr our website and these are stored in django source code

# accounts/login/[name='login']
# accounts/logout/[namee='logout']
# accounts/password_change/[name='password_change']
# accounts/password_change/done/[name='password_change_done']
# accounts/password_reset/[name='password_reset']
# accounts/reset/done/[name='password_reset_done']
# accounts/<uidb64>/<token>[name='password_reset_confirm']
# accounts/reset/done/[name='password_reset_complete']

