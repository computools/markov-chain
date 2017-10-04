from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions

class TextForm(forms.Form):
    text_type_choices = (('custom', "Custom"), ("python", "Python"))
    text = forms.CharField(widget=forms.Textarea, required=False)
    num = forms.IntegerField(max_value=500, initial=200, label="Text size")
    text_type = forms.ChoiceField(choices=text_type_choices)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-12'
    helper.layout = Layout(
        Field('text', css_class='input-sm'),
        Field('num', css_class='input-sm'),
        Field('text_type', css_class='input-sm'),
        FormActions(Submit('purchase', 'Generate Pseudo-Random Text', css_class='btn btn-primary btn-lg btn-block'))
        )

