from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from ppg_analyser.digitaltwin.patient_individual import calculate_patient_score

from .models import DocterOf, AccesTo

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home_view(request):
    return render(request,"index.html")

def info_view(request):
    return render(request, "information.html")

@login_required
def dashboard_view(request):
    if request.user in [d.docter for d in DocterOf.objects.all()]:
        return render(request, "overview_docter.html")
    
    context = {"patient": request.user}

    if has_ScoreModel(request.user):
        if request.user.ScoreModel.value:
            us = request.user
            ppgm = request.user.ppg_data.last()
            current_score = us.ScoreModel.value
            score_with_good_bmi = calculate_patient_score(
                20, us.ads.last().score, us.cds.last().score, ppgm.rmssd, ppgm.pnn50, ppgm.lfhf)
            score_with_good_ads = calculate_patient_score(
                us.bmi.last().bmi, 0, us.cds.last().score, ppgm.rmssd, ppgm.pnn50, ppgm.lfhf)
            score_with_good_cds = calculate_patient_score(
                us.bmi.last().bmi, us.ads.last().score, 12, ppgm.rmssd, ppgm.pnn50, ppgm.lfhf)
            score_with_good_ads_cds = calculate_patient_score(
                us.bmi.last().bmi, 0, 12, ppgm.rmssd, ppgm.pnn50, ppgm.lfhf)

            bmi_improvement = (current_score - score_with_good_bmi) / score_with_good_bmi
            ads_improvement = (current_score - score_with_good_ads) / score_with_good_ads
            cds_improvement = (current_score - score_with_good_cds) / score_with_good_cds
            ads_cds_improvement = (current_score - score_with_good_ads_cds) / score_with_good_ads_cds

            riskhtmls = []

            if bmi_improvement > 0.05:
                riskhtmls.append("<p>If you would have a BMI between 18.5 and 25 your risk would be decreased by: <span style='color: var(--green)'>{:.1%}</span></p>".format(bmi_improvement))
            if ads_improvement > 0.05:
                riskhtmls.append("<p>If you would stop drinking your risk would be decreased by: <span style='color: var(--green)'>{:.1%}</span></p>".format(ads_improvement))
            if cds_improvement > 0.05:
                riskhtmls.append("<p>If you would stop smoking your risk would be decreased by: <span style='color: var(--green)'>{:.1%}</span></p>".format(cds_improvement))
            if ads_improvement > 0.05 and cds_improvement > 0.05:
                riskhtmls.append("<p>If you would stop drinking AND smoking your risk would be decreased by: <span style='color: var(--green)'>{:.1%}</span></p>".format(ads_cds_improvement))

            if bmi_improvement <= 0.05 and ads_cds_improvement <=0.05:
                riskhtmls.append("<p>There is no indication that your lifestyle needs to change</p>")

            context["Risk_html"] = riskhtmls

        try:
            request.user.accesto
        except ObjectDoesNotExist:
            atm = AccesTo(request.user)

            atm.save()

    return render(request, "overview_patient.html", context)

@login_required
def detailed_patient_view(request, user_id):
    context = {
        "patient": User.objects.filter(id=user_id)[0]
    }
    return render(request, "detailed_docter.html", context)


def has_ScoreModel(user):
    try:
        user.ScoreModel
        return True
    except ObjectDoesNotExist:
        return False