from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

from ppg_analyser.digitaltwin.patient_individual import patient_score
# Create your models here.

class ScoreModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True)

    @staticmethod
    def calculate_score(user):
        ads = user.ads.last()
        cds = user.cds.last()
        bmi = user.bmi.last()
        ppg = user.ppg_data.last()

        try:
            sm = user.scoremodel
        except ObjectDoesNotExist:
            sm = ScoreModel.objects.create(user = user)

        print(ads, cds, bmi, ppg)

        if bmi and ads and cds and ppg:
            scores = patient_score(
                [bmi.bmi, 
                ads.score,
                cds.score,
                ppg.rmssd if ppg.rmssd else 0,
                ppg.pnn50 if ppg.pnn50 else 0,
                ppg.lfhf if ppg.lfhf else 0 ]
            )
            sm.value = scores[-1]
        sm.save()

    @staticmethod
    def placeholder(self, adsc, cdsc, ppgc):
        return adsc + cdsc + ppgc

class DocterOf(models.Model):
    docter = models.OneToOneField(User, on_delete=models.CASCADE)
    patient = models.ManyToManyField(User, related_name='DocterOf')

    def patients(self):
        return ", ".join([str(p) for p in self.patient.all()])

class AccesTo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ADS = models.BooleanField(default=True)
    CDS = models.BooleanField(default=True)
    BMI = models.BooleanField(default=True)