from django.shortcuts import render

from django.views.generic import View
from demo.demo_form import DemoForm
from demo.models import Book


class Index(View):
    TEMPLATE_PATH = 'demo/index.html'
    form = DemoForm

    def get(self, request):
        form = DemoForm()

        books = Book.objects.all()
        return render(request, self.TEMPLATE_PATH, {'form': form, 'books': books})

    def post(self, request):
        form = DemoForm(request.POST, request.FILES)

        form.submit()

        return self.get(request)





