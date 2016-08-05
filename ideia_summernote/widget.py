import json
from django.conf import settings
from django import forms
from django.shortcuts import render
from django.utils.safestring import mark_safe

__author__ = 'phillip'

SUMMERNOTE_DEFAULT_CONFIG = {

    'assets': {
        'js': (
            'https://code.jquery.com/jquery-2.2.4.min.js',
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.1/summernote.min.js', ),

        'css': {
            'all': (
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.1/summernote.css',
            )
        }
    },

    'editors': {
        'default': {
            'airMode': False,
            'toolbar': [
                ['style', ['bold', 'italic', 'underline', 'clear']],
                ['font', ['strikethrough', 'superscript', 'subscript']],
                ['fontsize', ['fontsize']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['height', ['height']]
            ],
            'popover': {
                'air':[
                    ['para', ['ul', 'ol', 'paragraph']],
                ]
            }
        },

    }
}

class SummernoteWidget(forms.Textarea):

    class Media:
        js = (
            'http://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.1/summernote.js',
            # settings.STATIC_URL + 'ckeditor/ckeditor-init.js',
        )

    def _media(self):
        return forms.Media(css=self.assets.get('css'),
                           js=self.assets.get('js'))
    media = property(_media)


    def __init__(self, editor_conf=None, plugins=None, *args, **kwargs):
        self.editor_conf=editor_conf
        self.plugins = plugins

        self.general_config = getattr(settings, 'SUMMERNOTE_CONFIG', SUMMERNOTE_DEFAULT_CONFIG)
        self.editors = self.general_config.get('editors')

        self.assets = self.general_config.get('assets', SUMMERNOTE_DEFAULT_CONFIG.get('assets'))


        super(SummernoteWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):


        return mark_safe(render(None, 'ideia_summernote/default.html', { 'self': self,
                                                                        'name': name,
                                                                        'config': json.dumps(self.editor_conf)
                                                                        }).content)