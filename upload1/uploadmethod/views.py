import os
from django.conf import settings
from django.http import HttpResponse,Http404
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import uploadFileForm

def uploadtxtfiles(request):
       #return HttpResponse('Hello_WOrld')
       if request.method == 'POST':
       	doc = request.FILES['document']
       	fs = FileSystemStorage()
       	filename = fs.save(doc.name,doc)
       	return HttpResponse (doc.name)
       return render(request,'uploadmethod/upload.html')
