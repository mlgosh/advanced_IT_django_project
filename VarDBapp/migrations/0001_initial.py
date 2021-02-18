# Generated by Django 3.1.6 on 2021-02-18 12:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('evidence_code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('gene_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('chrom', models.CharField(choices=[('Chr1', 'Chr1'), ('Chr2', 'Chr2'), ('Chr3', 'Chr3'), ('Chr4', 'Chr4'), ('Chr5', 'Chr5'), ('Chr6', 'Chr6'), ('Chr7', 'Chr7'), ('Chr8', 'Chr8'), ('Chr9', 'Chr9'), ('Chr10', 'Chr10'), ('Chr11', 'Chr11'), ('Chr12', 'Chr12'), ('Chr13', 'Chr13'), ('Chr14', 'Chr14'), ('Chr15', 'Chr15'), ('Chr16', 'Chr16'), ('Chr17', 'Chr17'), ('Chr18', 'Chr18'), ('Chr19', 'Chr19'), ('Chr20', 'Chr20'), ('Chr21', 'Chr21'), ('Chr22', 'Chr22'), ('ChrX', 'ChrX'), ('ChrY', 'ChrY')], max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('genome_build', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name=[('GRCh38', 'GRCh38'), ('GRCh37', 'GRCh37')])),
                ('description', models.TextField(blank=True, null=True)),
                ('version', models.CharField(max_length=10)),
                ('source', models.URLField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pathogenicity',
            fields=[
                ('pathogenicity_id', models.AutoField(primary_key=True, serialize=False)),
                ('pathogenicity_code', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('evidence_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.evidence')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10)),
                ('age', models.IntegerField(max_length=3)),
                ('proband', models.BooleanField(blank=True, null=True)),
                ('affected_relatives', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('phenotype_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('stage', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Sequencer',
            fields=[
                ('sequencer_id', models.AutoField(primary_key=True, serialize=False)),
                ('sequencer', models.CharField(max_length=10)),
                ('seq_model', models.CharField(max_length=50)),
                ('software_version', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('transcript', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('gene_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.gene')),
            ],
        ),
        migrations.CreateModel(
            name='Variant_description',
            fields=[
                ('variant_id', models.AutoField(primary_key=True, serialize=False)),
                ('variant_cDNA', models.CharField(max_length=40)),
                ('variant_protein', models.CharField(max_length=40)),
                ('variant_genome', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('genome_build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.genome')),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.transcript')),
            ],
        ),
        migrations.CreateModel(
            name='Variant_instance',
            fields=[
                ('instance_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('pathogenicity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.pathogenicity')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.patient')),
                ('sequencer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.sequencer')),
                ('variant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.variant_description')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='phenotype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VarDBapp.phenotype'),
        ),
    ]