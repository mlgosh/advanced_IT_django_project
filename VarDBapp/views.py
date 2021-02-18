from django.shortcuts import render
from django.utils import timezone
from .models import *

# Create your views here.
def home_page(request):
    return render(request, 'VarDBapp/home_page.html', {})

def file_upload(request):
    return render(request, 'VarDBapp/file_upload.html', {})

def single_upload(request):
	return render(request, 'VarDBapp/single_upload.html', {})

def browse_variants(request):
	return render(request, 'VarDBapp/browse_variants.html', {})

def search_result(request, search_term):
	return render(request, 'VarDBapp/search_result.html', {})

def variant_browser(request):
	return render(request, 'VarDBapp/variant_browser.html', {})

def edit_variant(request):
	return render(request, 'VarDBapp/edit_variant.html', {})

def edit_sample(request):
	return render(request, 'VarDBapp/edit_sample.html', {})