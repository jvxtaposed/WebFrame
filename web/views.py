from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
# Create your views here.

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from web.models import Document
from web.forms import DocumentForm
from colcounter import colCount
import os


def home(request):
    documents = Document.objects.all()
    return render(request, 'web/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        out = colCount.cnt(filename)
		#image = results(None)
        return render(request, 'results.html', {
        	'out':[ out]
        })
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def home(request):
	template = loader.get_template('home.html')
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		out = colCount.cnt(filename)
		#image = results(None)
		return render(request, 'results.html', {
			'out':[ out]
			})

	return render(request, 'home.html')

def about(request):
	template = loader.get_template('about.html')
	context = {

	}
	return HttpResponse(template.render(context,request))

def projects(request):
	template = loader.get_template('projects.html')
	context={

	}
	return HttpResponse(template.render(context,request))

def contact(request):
	template = loader.get_template('contact.html')
	context={

	}
	return HttpResponse(template.render(context,request))

def results(request):
	template = loader.get_template('results.html')
	context={

	}
	return HttpResponse(template.render(context,request))

