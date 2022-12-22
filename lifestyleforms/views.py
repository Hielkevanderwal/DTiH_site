from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import ADSModel, CDSModel, BMIModel
from .forms import ADSForm, CDSForm, BMIForm, readonly_ADSForm, readonly_CDSForm

form_types = {
    "ADS": [ADSModel, ADSForm, readonly_ADSForm],
    "CDS": [CDSModel, CDSForm, readonly_CDSForm],
    "BMI": [BMIModel, BMIForm],
}

@login_required
def form_view(request, form_type, user_id = None):

    user_obj = User.objects.get(id = user_id) if user_id else request.user

    if request.POST:
        form = form_types[form_type][1](request.POST)
        if True:
            obj = form.save(commit=False)
            obj.user = user_obj
            obj.save()
        return redirect('dashboard')
    context = {"form": form_types[form_type][1]}
    return render(request, "form_view.html", context)
    
def formviewer_view(request, form_type, form_id):

    item = get_object_or_404(form_types[form_type][0], id=form_id)
    form = form_types[form_type][2](instance = item)

    return render(request, "form_view.html", context={
        "form": form,
    })
