from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Raw_ppg_data, CDSModel, ADSModel

class ADSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = ADSModel
        fields = "__all__"
        widgets = {
            "q1": forms.RadioSelect(),
            "q2": forms.RadioSelect(),
            "q3": forms.RadioSelect(),
            "q4": forms.RadioSelect(),
            "q5": forms.RadioSelect(),
            "q6": forms.RadioSelect(),
            "q7": forms.RadioSelect(),
            "q8": forms.RadioSelect(),
            "q9": forms.RadioSelect(),
            "q10": forms.RadioSelect(),
            "q11": forms.RadioSelect(),
            "q12": forms.RadioSelect(),
            "q13": forms.RadioSelect(),
            "q14": forms.RadioSelect(),
            "q15": forms.RadioSelect(),
            "q16": forms.RadioSelect(),
            "q17": forms.RadioSelect(),
            "q18": forms.RadioSelect(),
            "q19": forms.RadioSelect(),
            "q20": forms.RadioSelect(),
            "q21": forms.RadioSelect(),
            "q22": forms.RadioSelect(),
            "q23": forms.RadioSelect(),
            "q24": forms.RadioSelect(),
            "q25": forms.RadioSelect(),
            "q26": forms.RadioSelect(),
            "q27": forms.RadioSelect(),
            "q28": forms.RadioSelect(),
            "q29": forms.RadioSelect(),
        }
   

    

class CDSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = CDSModel
        fields = "__all__"
        widgets = {
            "q4": forms.RadioSelect(),
            "q5": forms.RadioSelect(),
            "q6": forms.RadioSelect(),
            "q7": forms.RadioSelect(),
            "q8": forms.RadioSelect(),
            "q9": forms.RadioSelect(),
            "q10": forms.RadioSelect(),
            "q11": forms.RadioSelect(),
            "q12": forms.RadioSelect(),
        }


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