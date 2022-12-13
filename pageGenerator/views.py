from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

from .forms import ADSForm, CDSForm, Data_upload_form

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
    print(request.user.ads.all())
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

@login_required
def ADSForm_view(request):
    if request.POST:
        form = ADSForm(request.POST)
        if True:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('loginhandler')
    context = {"form": ADSForm}
    return render(request, "form_view.html", context)


@login_required
def CDSForm_view(request):
    if request.POST:
        form = CDSForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('loginhandler')
    context = {"form": CDSForm}
    return render(request, "form_view.html", context)

@login_required
def uploadCSV_view(request):
    if request.POST:
            form = Data_upload_form(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
            return redirect('loginhandler')
    context = {"form": Data_upload_form}
    return render(request, "form_view.html", context)
