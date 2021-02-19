from django import forms
from django.forms import ModelForm
from .models import *

class Variant_description_form(ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Variant_description
		fields = '__all__'

class Variant_instance_form(ModelForm):
	required_css_class = 'required'
	class Meta:
		model = Variant_instance
		fields = '__all__'