from django.forms.fields import CharField
from django_ideia_summernote.widget import SummernoteWidget

__author__ = 'phillip'


class SummernoteFormField(CharField):


    def __init__(self, editor_conf='default', load_assets=True, plugins=None, *args, **kwargs):

        self.load_assets=load_assets
        kwargs.update({'widget': SummernoteWidget(editor_conf=editor_conf, load_assets=self.load_assets, plugins=plugins)})
        super(SummernoteFormField, self).__init__(*args, **kwargs)

