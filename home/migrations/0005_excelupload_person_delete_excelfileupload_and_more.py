# Generated by Django 5.1.1 on 2024-09-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel_uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('SPOC', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('jobcode', models.CharField(max_length=100)),
                ('Candidatecode', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=100)),
                ('TEX', models.CharField(max_length=100)),
                ('REX', models.CharField(max_length=100)),
                ('Employer', models.CharField(max_length=100)),
                ('PCTC', models.CharField(max_length=100)),
                ('ECTC', models.CharField(max_length=100)),
                ('Notice', models.CharField(max_length=100)),
                ('IntvDate', models.CharField(max_length=100)),
                ('IntvTIme', models.CharField(max_length=100)),
                ('IntvMode', models.CharField(max_length=100)),
                ('Remarks', models.CharField(max_length=100)),
                ('ConfirmedProjection', models.CharField(max_length=100)),
                ('Doj', models.CharField(max_length=100)),
                ('OfferedCTC', models.CharField(max_length=100)),
                ('VariableCTC', models.CharField(max_length=100)),
                ('BillingPrecentage', models.CharField(max_length=100)),
                ('BillingValue', models.CharField(max_length=100)),
                ('GrossProfit', models.CharField(max_length=100)),
                ('NetProfit', models.CharField(max_length=100)),
                ('RecruterPayout', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Excelfileupload',
        ),
        migrations.DeleteModel(
            name='Phonenumber',
        ),
    ]
