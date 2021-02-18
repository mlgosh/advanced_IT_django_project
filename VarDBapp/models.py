from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Gene(models.Model):
    gene_name = models.CharField(max_length=10, primary_key=True)
    CHROMOSOME_CHOICES = [('Chr1', 'Chr1'), ('Chr2', 'Chr2'), ('Chr3', 'Chr3'), ('Chr4', 'Chr4'), ('Chr5', 'Chr5'), ('Chr6', 'Chr6'), ('Chr7', 'Chr7'), ('Chr8', 'Chr8'), ('Chr9', 'Chr9'), ('Chr10', 'Chr10'), ('Chr11', 'Chr11'), ('Chr12', 'Chr12'), ('Chr13', 'Chr13'), ('Chr14', 'Chr14'), ('Chr15', 'Chr15'), ('Chr16', 'Chr16'), ('Chr17', 'Chr17'), ('Chr18', 'Chr18'), ('Chr19', 'Chr19'), ('Chr20', 'Chr20'), ('Chr21', 'Chr21'), ('Chr22', 'Chr22'), ('ChrX', 'ChrX'), ('ChrY', 'ChrY')]
    chrom = models.CharField(choices=CHROMOSOME_CHOICES, unique=True, max_length=5)
    # STRAND_CHOICES = [('+', '+'), ('-', '-')]
    # strand = models.CharField(choices=STRAND_CHOICES, max_length=1, unique=True)

    def __str__(self):
        return self.gene_name

class Transcript(models.Model):
    transcript = models.CharField(max_length=15, primary_key=True)
    gene_name = models.ForeignKey(Gene, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.transcript

class Genome(models.Model):
    ASSEMBLY_CHOICES = [('GRCh38', 'GRCh38'), ('GRCh37', 'GRCh37')]
    genome_build = models.CharField(ASSEMBLY_CHOICES, unique=True, max_length=6, primary_key=True)
    description = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=10)
    source = models.URLField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genome_build

class Variant_description(models.Model):
    variant_id = models.AutoField(primary_key=True)
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE)
    variant_cDNA = models.CharField(max_length=40)
    variant_protein = models.CharField(max_length=40)
    variant_genome = models.CharField(max_length=40)
    genome_build = models.ForeignKey(Genome, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    # ADD FUNCTION TO VALIDATE THE cDNA, protein and genome NAMES

    def __str__(self):
        return self.variant_id

class Evidence(models.Model):
    evidence_code = models.CharField(primary_key=True, max_length=4)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.evidence_code

class Pathogenicity(models.Model):
    pathogenicity_id = models.AutoField(primary_key=True)
    CODE_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    pathogenicity_code = models.IntegerField(choices=CODE_CHOICES, unique=True)
    evidence_code = models.ForeignKey(Evidence, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pathogenicity_id

class Sequencer(models.Model):
    sequencer_id = models.AutoField(primary_key=True)
    sequencer = models.CharField(max_length=10)
    seq_model = models.CharField(max_length=50)
    software_version = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sequencer

class Phenotype(models.Model):
    phenotype_id = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    stage = models.CharField(max_length=6)

    def __str__(self):
        return self.phenotype_id

class Patient(models.Model):
    patient_id = models.CharField(max_length=10)
    phenotype_id = models.ForeignKey(Phenotype, on_delete=models.CASCADE)
    age = models.IntegerField()
    proband = models.BooleanField(null=True, blank=True)
    affected_relatives = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.patient_id

class Variant_instance(models.Model):
    instance_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    variant_id = models.ForeignKey(Variant_description, on_delete=models.CASCADE)
    pathogenicity_id = models.ForeignKey(Pathogenicity, on_delete=models.CASCADE)
    sequencer_id = models.ForeignKey(Sequencer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(timezone.now)