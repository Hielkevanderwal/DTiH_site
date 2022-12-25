from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import DocterOf

# Create your views here.
def home_view(request):
    return render(request,"index.html")

def info_view(request):
    return render(request, "information.html")

@login_required
def dashboard_view(request):
    if request.user in [d.docter for d in DocterOf.objects.all()]:
        return render(request, "overview_docter.html")

    return render(request, "overview_patient.html")

@login_required
def detailed_patient_view(request, user_id):
    context = {
        "patient": User.objects.filter(id=user_id)[0]
    }
    return render(request, "detailed_docter.html", context)