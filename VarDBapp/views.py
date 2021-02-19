from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def home_page(request):
    return render(request, 'VarDBapp/home_page.html', {})

@login_required
def file_upload(request):
    return render(request, 'VarDBapp/file_upload.html', {})

@login_required
def single_upload(request):
        if request.method == 'POST': # If the form has been submitted
            Variant_description = Variant_description_form(request.POST)
            if Variant_description.is_valid(): # All validation rules pass
                    description = Variant_description.save()
                    return HttpResponseRedirect('Successful')
        else:
            Variant_description = Variant_description_form()
        
        context = {
            'Variant_description': Variant_description,
            }

        return render(request, 'VarDBapp/single_upload.html', context)

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

