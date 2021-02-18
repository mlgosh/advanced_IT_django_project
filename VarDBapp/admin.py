from django.contrib import admin
from .models import Gene, Transcript, Genome, Variant_description, Evidence, Pathogenicity, Sequencer, Phenotype, Patient, Variant_instance

# Register your models here.
admin.site.register(Gene)
admin.site.register(Transcript)
admin.site.register(Genome)
admin.site.register(Variant_description)
admin.site.register(Evidence)
admin.site.register(Pathogenicity)
admin.site.register(Sequencer)
admin.site.register(Phenotype)
admin.site.register(Patient)
admin.site.register(Variant_instance)