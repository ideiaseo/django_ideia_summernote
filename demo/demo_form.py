from django.forms import forms
from demo.models import Book

from ideia_summernote.fields import SummernoteFormField

__author__ = 'phillip'



class DemoForm(forms.Form):

    text = SummernoteFormField(editor_conf='comment')


    def submit(self):

        if self.is_valid():
            return self.__proccess__()
        else:
            print self.errors
            return None

    def __proccess__(self):
        book = Book(title='title', text=self.cleaned_data['text'])
        book.save()

        print book
        return book