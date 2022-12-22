from django.urls import path

from . import views

urlpatterns = [
    path('<str:form_type>/', views.form_view),
    path('<str:form_type>/<int:user_id>/', views.form_view),
    path('<str:form_type>/answers/<int:form_id>/', views.formviewer_view, name="form_viewer_url")
]