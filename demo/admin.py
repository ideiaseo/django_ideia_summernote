from django.contrib import admin
from django import forms
from demo.models import Book
from ideia_summernote.widget import SummernoteWidget


class BookAdminForm(forms.ModelForm):
    class Meta:
        widgets = {'text': SummernoteWidget(editor_conf='another')}
        excludes = ()

class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

admin.site.register(Book, BookAdmin)