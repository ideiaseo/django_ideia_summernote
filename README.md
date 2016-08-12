## Django Ideia Summernote ##
----------
A django summernote integration based [Django Ckeditor](https://github.com/django-ckeditor/django-ckeditor).
### Installation ###
----------

 1. Install Django Ideia Summernote

```bash
    $ pip install django-ideia-summernote
```
2. Add ideia_summernote into *INSTALLED_APPS*
```python
   INSTALLED_APPS = [
   # another apps
   'ideia_summernote'
]
```
3. Add the summernote field into your form
 
 ```python
 from ideia_summernote.fields import SummernoteFormField
 
 class BookForm(forms.Form):
		text = SummernoteFormField()
```
... or directly on Model

```python
from ideia_summernote.fields import SummernoteField

class Book(models.Model):
        text = SummernoteField()
```

... or just changing the widget field

```python
from django import forms

 class BookForm(forms.Form):
		text = forms.Textarea(widget=SummernoteWidget())
```
### Configuration ###
----------
By default, some basic summernote settings were loaded, but it is possible set your own. Bellow, there a commented full example:
```python

_2_MB = 2048000

# To set your own configuration, a var named SUMMERNOTE_CONFIG must be set.
SUMMERNOTE_CONFIG = {

    'restrict_to_user': True, # If the upload images are restrict by authenticated users 
    'use_path_user': True, # If the upload image folder must have the username as name
    'maximum_image_upload': _2_MB, # Setting the maximum upload image size for validation
    
    # Here it is possible to set your own assets, but remember that jQuery and Bootstrap are dependencies.
    'assets': {
        
        'js': (
            'https://code.jquery.com/jquery-2. 2.4.min.js',  
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.1/summernote.min.js', ),

        'css': {
            # css media (print, all, etc)
            'all': (
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
                'https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.1/summernote.css',
            )
        }
    },
     
     # Defining different configuration editors
    'editors': {
        # Some editor name to be referenced Ex: (text = SummernoteFormField(editor_conf='default'))
        'default': {
            # Summernote configs, see: link
            'airMode': False,
            'toolbar': [
                ['style', ['bold', 'italic', 'underline', 'clear']],
                ['font', ['strikethrough', 'superscript', 'subscript']],
                ['fontsize', ['fontsize']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['height', ['height']],
                ['picture', ['picture']],
                ['codeview', ['codeview']]
            ],
            'enabledTags': {
                'pre': ['style'],
                'p': ['style']
            },
            'enabledStyles':[
                'text-align', 'font-size', 'line-height', 'background-color', 'width', 'height',
            ],
            'popover': {
                'air':[
                    ['para', ['ul', 'ol', 'paragraph']],
                ],
                'image': [
                ['imagesize', ['imageSize100', 'imageSize50', 'imageSize25']],
                ['float', ['floatLeft', 'floatRight', 'floatNone']],
                ['remove', ['removeMedia']]
              ]
            }
        },
        'another_editor': {
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
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                ['font', ['strikethrough', 'superscript', 'subscript']],
                ['fontsize', ['fontsize']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['height', ['height']]
                ]
            }
        },

    }
}
```

