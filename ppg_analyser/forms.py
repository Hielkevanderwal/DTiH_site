from django import forms
from .models import Raw_ppg_data, Processed_ppg_data

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Fieldset


class Data_upload_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Submit'))
    
    class Meta:
        model = Raw_ppg_data
        fields = ['csv_file']

    forms.FileField(
        label="CSV file"
    )

class ReadOnlyPPGForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper(self)
        self.helper.layout = (
            Fieldset(
                Field("bpm", disabled=True),
                Field("bpm", disabled = False),
                Field("ibi", disabled = True),
                Field("sdnn", disabled = True),
                Field("sdsd", disabled = True),
                Field("rmssd", disabled = True),
                Field("pnn20", disabled = True),
                Field("pnn50", disabled = True),
                Field("hr_mad", disabled = True),
                Field("sd1", disabled = True),
                Field("sd2", disabled = True),
                Field("s", disabled = True),
                Field("sd1sd2", disabled = True),
                Field("breathingrate", disabled = True),
                Field("vlf", disabled = True),
                Field("lf", disabled = True),
                Field("hf", disabled = True),
                Field("lfhf", disabled = True),
                Field("p_total", disabled = True),
                Field("vlf_perc", disabled = True),
                Field("hf_prec", disabled = True),
                Field("lf_nu", disabled = True),
                Field("hf_nu", disabled = True),
            )
        )

    class Meta:
        model = Processed_ppg_data
        fields = "__all__"

    
