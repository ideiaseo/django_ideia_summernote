from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from ideia_summernote.ideia_forms import UploadImageForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
class Upload(View):

    def post(self, request):

        file = request.FILES['file']

        path = os.path.join(settings.MEDIA_ROOT, file.name)

        path = default_storage.save(path, file)

        return JsonResponse(data={'url': os.path.join(settings.MEDIA_URL, file.name)})