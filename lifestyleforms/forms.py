from django import forms
from crispy_forms.helper import FormHelper #noqa
from crispy_forms.layout import Submit, Field, Fieldset #noqa

from .models import CDSModel, ADSModel, BMIModel

class readonly_ADSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = (
            Fieldset(
                Field('q1', disabled=True),
                Field('q2', disabled=True),
                Field('q3', disabled=True),
                Field('q4', disabled=True),
                Field('q5', disabled=True),
                Field('q6', disabled=True),
                Field('q7', disabled=True),
                Field('q8', disabled=True),
                Field('q9', disabled=True),
                Field('q10', disabled=True),
                Field('q11', disabled=True),
                Field('q12', disabled=True),
                Field('q13', disabled=True),
                Field('q14', disabled=True),
                Field('q15', disabled=True),
                Field('q16', disabled=True),
                Field('q17', disabled=True),
                Field('q18', disabled=True),
                Field('q19', disabled=True),
                Field('q20', disabled=True),
                Field('q21', disabled=True),
                Field('q22', disabled=True),
                Field('q23', disabled=True),
                Field('q24', disabled=True),
                Field('q25', disabled=True),
                Field('q26', disabled=True),
                Field('q27', disabled=True),
                Field('q28', disabled=True),
                Field('q29', disabled=True),
            )
        )

    class Meta:
        model = ADSModel
        fields = "__all__"

class readonly_CDSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = (
            Fieldset(
                Field('q1', disabled=True),
                Field('q2', disabled=True),
                Field('q3', disabled=True),
                Field('q4', disabled=True),
                Field('q5', disabled=True),
                Field('q6', disabled=True),
                Field('q7', disabled=True),
                Field('q8', disabled=True),
                Field('q9', disabled=True),
                Field('q10', disabled=True),
                Field('q11', disabled=True),
                Field('q12', disabled=True),
            )
        )

    class Meta:
        model = CDSModel
        fields = "__all__"

class BMIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = BMIModel
        fields = ['height','mass']

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