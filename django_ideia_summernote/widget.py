from django.forms import Textarea
from django.shortcuts import render
from django.utils.safestring import mark_safe

__author__ = 'phillip'



class SummernoteWidget(Textarea):

    def __init__(self, editor_conf=None, plugins=None, *args, **kwargs):
        super(SummernoteWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):


        return mark_safe(render(None, 'ideia_summernote/default.html', {'name': name,}).content)