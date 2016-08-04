from django.shortcuts import render

from django.views.generic import View
from demo.demo_form import DemoForm


class Index(View):
    TEMPLATE_PATH = 'demo/index.html'
    form = DemoForm

    def get(self, request):
        form = self.form()

        return render(request, self.TEMPLATE_PATH, {'form': form})
