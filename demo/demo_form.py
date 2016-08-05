from django.forms import forms

from ideia_summernote.fields import SummernoteFormField

__author__ = 'phillip'



class DemoForm(forms.Form):

    text = SummernoteFormField(editor_conf='comment')

    another_text = SummernoteFormField(editor_conf='another')