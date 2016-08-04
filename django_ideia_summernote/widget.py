import json
from django.forms import Textarea
from django.shortcuts import render
from django.utils.safestring import mark_safe

__author__ = 'phillip'

DEFAULT_EDITOR = {
    'airMode': True,
    'toolbar': [
        # ['style', ['bold', 'italic', 'underline', 'clear']],
        # ['font', ['strikethrough', 'superscript', 'subscript']],
        # ['fontsize', ['fontsize']],
        # ['color', ['color']],
        # ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']]
    ],
    'popover': {
        'air':[
            ['para', ['ul', 'ol', 'paragraph']],
        ]
    }
}

class SummernoteWidget(Textarea):

    def __init__(self, editor_conf=None, plugins=None, *args, **kwargs):
        super(SummernoteWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):
        print json.dumps(DEFAULT_EDITOR)
        return mark_safe(render(None, 'ideia_summernote/default.html', {'name': name, 'config': json.dumps(DEFAULT_EDITOR)}).content)