import json
from django.conf import settings
from django import forms
from django.shortcuts import render
from django.utils.safestring import mark_safe

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
        )

    def _media(self):
        js = self.assets.get('js')
        if self.load_init:
            js+= (settings.STATIC_URL + 'js/summernote-init.js',)
        return forms.Media(css=self.assets.get('css'),
                           js=js)
    media = property(_media)


    def __init__(self, editor_conf=None, load_init=True, async=None, plugins=None, *args, **kwargs):

        self.plugins = plugins
        self.load_init = load_init
        self.async = async
        self.general_config = getattr(settings, 'SUMMERNOTE_CONFIG', SUMMERNOTE_DEFAULT_CONFIG)
        self.editors = self.general_config.get('editors')
        self.editor_conf=self.editors.get(editor_conf or 'default', self.editors.get('default'))


        self.assets = self.general_config.get('assets', SUMMERNOTE_DEFAULT_CONFIG.get('assets'))


        super(SummernoteWidget, self).__init__(*args, **kwargs)


    def render(self, name, value, attrs=None):

        return mark_safe(render(None, 'ideia_summernote/default.html', { 'self': self,
                                                                        'name': name,
                                                                         'value': value,
                                                                        'async': self.async,
                                                                        'config': json.dumps(self.editor_conf)
                                                                        }).content)