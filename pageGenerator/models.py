import math

from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

from ppg_analyser.digitaltwin.patient_individual import calculate_patient_score
# Create your models here.

class ScoreModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ScoreModel')
    value = models.IntegerField(blank=True, null=True)

    @staticmethod
    def calculate_score(user):
        ads = user.ads.last()
        cds = user.cds.last()
        bmi = user.bmi.last()
        ppg = user.ppg_data.last()

        try:
            sm = user.ScoreModel
        except ObjectDoesNotExist:
            sm = ScoreModel.objects.create(user = user)

        if bmi and ads and cds and ppg:
            sm.value = calculate_patient_score(bmi.bmi, ads.score, cds.score, ppg.rmssd, ppg.pnn50, ppg.lfhf)
        sm.save()

    @staticmethod
    def placeholder(self, adsc, cdsc, ppgc):
        return adsc + cdsc + ppgc

class DocterOf(models.Model):
    docter = models.OneToOneField(User, on_delete=models.CASCADE)
    patient = models.ManyToManyField(User, related_name='DocterOf')

    def patients(self):
        return ", ".join([str(p) for p in self.patient.all()])

    def __str__(self):
        return "Dr. {}".format(self.docter)

class AccesTo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ADS = models.BooleanField(default=True)
    CDS = models.BooleanField(default=True)
    BMI = models.BooleanField(default=True)

    def __str__(self):
        return "Acces model {}".format(self.user)