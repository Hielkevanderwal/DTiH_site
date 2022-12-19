"""DTiH_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pageGenerator.views import home_view, dashboard_view, CDSForm_view, ADSForm_view, uploadCSV_view, detailed_patient_view, BMIForm_view

urlpatterns = [
    path('', home_view, name= 'home'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path('dashboard/', dashboard_view, name= 'dashboard'),

    path('patients/<int:user_id>', detailed_patient_view),

    # path('forms/<str:form_name>/', form_view),
    path('forms/CDS/', CDSForm_view),
    path('forms/ADS/', ADSForm_view),
    path('forms/BMI/', BMIForm_view),

    path('forms/uploadCSV/', uploadCSV_view),
    path('patients/<int:user_id>/upload/',uploadCSV_view)
] 

urlpatterns += staticfiles_urlpatterns()
