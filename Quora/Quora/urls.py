"""Quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls import url

from django_registration.backends.one_step.views import RegistrationView

from django.views.generic import TemplateView
from core.views import IndexTemplateView
from users.forms import CustomUserForm

from .views import home

# Create Two Step Registration Using This Documentation
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [

    path('admin/', admin.site.urls),
    
    # Register User Web Browser Path
    path("accounts/register/", RegistrationView.as_view(form_class=CustomUserForm, success_url="/seaviking/survey/question/"), name="django_registration_register"),

    # Register User Register One Step
    path("accounts/", include("django_registration.backends.one_step.urls")),

    # Login User Web Browser Path
    path("accounts/", include("django.contrib.auth.urls")),

    # Load Users API Endpoint Urls
    path("api/", include("users.api.urls")),

    path("api/", include("questions.api.urls")),

    # Load REST Framework 
    path("api-auth/", include("rest_framework.urls")),

    # REST Login Path
    path("api/rest_auth/", include("rest_auth.urls")),

    # REST Register Path
    path("api/rest_auth/register", include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),

    #url(r'/', home, name='home')

]

urlpatterns += [    
    path(r'^robots\.txt$', TemplateView.as_view(template_name="sysfiles/robots.txt", content_type='text/plain')),
]
