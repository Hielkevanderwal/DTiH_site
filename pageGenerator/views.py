from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import ADSForm, CDSForm, Data_upload_form, BMIForm
from .models import DocterOf


# Create your views here.
def home_view(request):
    return render(request,"index.html")

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
        return redirect('dashboard')
    context = {"form": CDSForm}
    return render(request, "form_view.html", context)

@login_required
def BMIForm_view(request):
    if request.POST:
        form = BMIForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('dashboard')
    context = {"form": BMIForm}
    return render(request, "form_view.html", context)

@login_required
def uploadCSV_view(request, user_id = None):
    
    user_obj = User.objects.get(id = user_id) if user_id else request.user

    if request.POST:
            form = Data_upload_form(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = user_obj
                obj.save()
            return redirect('dashboard')
    context = {"form": Data_upload_form}
    return render(request, "form_view.html", context)

def formviewer_view(request):
    return render(request, "formviewer.html")