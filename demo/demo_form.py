from django.forms import forms
from django_ideia_summernote.fields import SummernoteFormField

__author__ = 'phillip'



class DemoForm(forms.Form):

    text = SummernoteFormField(editor_conf='comment')