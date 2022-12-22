from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import Data_upload_form, ReadOnlyPPGForm
from .models import Processed_ppg_data

# Create your views here.

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

@login_required
def ppgviewer_view(request, form_id):

    item = get_object_or_404(Processed_ppg_data, id=form_id)
    form = ReadOnlyPPGForm(instance = item)

    return render(request, "form_view.html", context={
        "form": form,
    })