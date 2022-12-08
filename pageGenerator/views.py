from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    context = {
        "page_name": "home"
    }
    return render(request,"index.html",context)

@login_required
def login_complete(request):
    if(request.user.groups.filter(name='docters').exists()):
        return redirect("/d/dashboard/")

    return redirect("/p/dashboard/")

@login_required
def overview_docter_view(request):
    context = {
        "page_name": "dashboard"
    }
    return render(request, "overview_docter.html", context)

@login_required
def overview_patient_view(request):
    context = {
        "page_name": "dashboard"
    }
    return render(request, "overview_patient.html", context)

@login_required
def detailed_patient_view(request):
    context = {
        "page_name": "???"
    }
    return render(request, "detailed_docter.html", context)
