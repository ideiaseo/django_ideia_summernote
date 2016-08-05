from django.forms.fields import CharField

from ideia_summernote.widget import SummernoteWidget


class SummernoteFormField(CharField):


    def __init__(self, editor_conf='default', plugins=None, *args, **kwargs):

        kwargs.update({'widget': SummernoteWidget(editor_conf=editor_conf, plugins=plugins)})
        super(SummernoteFormField, self).__init__(*args, **kwargs)

