import json
from django.conf import settings
from django.forms import Textarea
from django.shortcuts import render
from django.utils.safestring import mark_safe

__author__ = 'phillip'

SUMMERNOTE_DEFAULT_CONFIG = {


    'editors': {
        'default': {
            'airMode': False,
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
        },
        'comment': {
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
    }


}

class SummernoteWidget(Textarea):

    def __init__(self, editor_conf=None, plugins=None, *args, **kwargs):
        self.editor_conf=editor_conf
        self.plugins = plugins
        super(SummernoteWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):
        general_config = getattr(settings, 'SUMMERNOTE_CONFIG', SUMMERNOTE_DEFAULT_CONFIG)
        editors = general_config.get('editors')
        editor_config = editors.get(self.editor_conf, editors.get('default'))
        assets = general_config.get('assets', SUMMERNOTE_DEFAULT_CONFIG.get('assets'))
        return mark_safe(render(None, 'ideia_summernote/default.html', {'name': name,
                                                                        'config': json.dumps(editor_config)
                                                                        }).content)