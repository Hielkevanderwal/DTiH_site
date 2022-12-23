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
                Field("bpm", disabled = True)
            )
        )

    class Meta:
        model = Processed_ppg_data
        fields = "__all__"

    
