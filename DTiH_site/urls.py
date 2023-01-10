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

from pageGenerator import views

urlpatterns = [
    path('', views.home_view, name= 'home'),

    path('dashboard/', views.dashboard_view, name= 'dashboard'),
    path('information/', views.info_view, name= 'information'),

    path('admin/', admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.SignUpView.as_view()),

    path("forms/", include("lifestyleforms.urls")),
    path("ppg/", include("ppg_analyser.urls")),

    path('patients/<int:user_id>', views.detailed_patient_view),
] 

urlpatterns += staticfiles_urlpatterns()
