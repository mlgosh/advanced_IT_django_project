from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'VarDBapp/home_page.html', {})

def file_upload(request):
    return render(request, 'VarDBapp/file_upload.html', {})

def single_upload(request):
	return render(request, 'VarDBapp/single_upload', {})

def browse_variants(request):
	return render(request, 'VarDBapp/browse_variants', {})

def search_result(request):
	return render(request, 'VarDBapp/search_result', {})

def variant_browser(request):
	return render(request, 'VarDBapp/variant_browser', {})

def edit_variant(request):
	return render(request, 'VarDBapp/edit_variant', {})

def edit_sample(request):
	return render(request, 'VarDBapp/edit_sample', {})