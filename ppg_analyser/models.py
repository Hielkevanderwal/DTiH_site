from django.db import models
from django.contrib.auth.models import User

from .digitaltwin.DTiH_read_excel_freesense import read_csv
from .digitaltwin.DTiH_annalyzing_ppg import peak_detection, preprocessing_ppg_signal

from pageGenerator.models import ScoreModel

# Create your models here.
class Raw_ppg_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    csv_file = models.FileField()
    created = models.DateTimeField(auto_now_add = True, editable=False)
    processed = models.BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        super(Raw_ppg_data, self).save(*args, **kwargs)
        ScoreModel.calculate_score(self.user)
        if not self.processed:
            self.process_ppg()

    def process_ppg(self):
        ppg_signal = read_csv(self.csv_file.path)
        filtered_signal = preprocessing_ppg_signal(ppg_signal, 400)
        _, measurements = peak_detection(filtered_signal, 400)

        ppg_obj = Processed_ppg_data.objects.create(
            user = self.user,
            raw_ppg_data_id = self,
            bpm = measurements['bpm'],
            ibi = measurements['ibi'],
            sdsd = measurements['sdsd'],
            sdnn = measurements['sdnn'],
            rmssd = measurements['rmssd'],
            pnn20 = measurements['pnn20'],
            pnn50 = measurements['pnn50'],
            hr_mad = measurements['hr_mad'],
            sd1 = measurements['sd1'],
            sd2 = measurements['sd2'],
            s = measurements['s'],
            sd1sd2 = measurements['sd1/sd2'],
            breathingrate = measurements['breathingrate'],
            vlf = measurements['vlf'],
            lf = measurements['lf'],
            hf = measurements['hf'],
            lfhf = measurements['lf/hf'],
            p_total = measurements['p_total'],
            vlf_perc = measurements['vlf_perc'],
            hf_perc = measurements['hf_perc'],
            lf_nu = measurements['lf_nu'],
            hf_nu = measurements['hf_nu'],
        )
        ppg_obj.save()
        self.processed = True
        self.save()

class Processed_ppg_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ppg_data", editable=False)
    raw_ppg_data_id = models.ForeignKey(Raw_ppg_data, on_delete=models.CASCADE, editable=False)
    finished_time = models.DateTimeField(auto_now=True)
    bpm = models.FloatField(blank=True, null=True, )
    ibi = models.FloatField(blank=True, null=True)
    sdnn = models.FloatField(blank=True, null=True)
    sdsd = models.FloatField(blank=True, null=True)
    rmssd = models.FloatField(blank=True, null=True)
    pnn20 = models.FloatField(blank=True, null=True)
    pnn50 = models.FloatField(blank=True, null=True)
    hr_mad = models.FloatField(blank=True, null=True)
    sd1 = models.FloatField(blank=True, null=True)
    sd2 = models.FloatField(blank=True, null=True)
    s = models.FloatField(blank=True, null=True)
    sd1sd2 = models.FloatField(blank=True, null=True)
    breathingrate = models.FloatField(blank=True, null=True)
    vlf = models.FloatField(blank=True, null=True)
    lf = models.FloatField(blank=True, null=True)
    hf = models.FloatField(blank=True, null=True)
    lfhf = models.FloatField(blank=True, null=True)
    p_total = models.FloatField(blank=True, null=True)
    vlf_perc = models.FloatField(blank=True, null=True)
    hf_perc = models.FloatField(blank=True, null=True)
    lf_nu = models.FloatField(blank=True, null=True)
    hf_nu = models.FloatField(blank=True, null=True)

    class Meta:
        get_latest_by = 'finished_time'