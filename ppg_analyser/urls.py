from django.urls import path

from . import views

urlpatterns = [
    path('uploadCSV/', views.uploadCSV_view, name= 'uploadcsv'),
    path('uploadCSV/<int:user_id>/', views.uploadCSV_view, name='uploadcsvu'),
    path('results/<int:form_id>/', views.ppgviewer_view, name= 'pgginfo'),
]