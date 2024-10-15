# models.py
from django.db import models

class ExcelUpload(models.Model):
    file = models.FileField(upload_to='excel_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Excel file uploaded on {self.uploaded_at}"

# models.py
class Person(models.Model):
    
    
    source = models.CharField(max_length=100, null = True, blank = True)
    Date = models.CharField(max_length=100, null = True, blank = True)
    client =models.CharField(max_length=100, null = True, blank = True)
    SPOC = models.CharField(max_length=100, null = True, blank = True)
    skill = models.CharField(max_length=100, null = True, blank = True)
    jobcode = models.CharField(max_length=100, null = True, blank = True)
    Candidatecode = models.CharField(max_length=100, null = True, blank = True)
    name =   models.CharField(max_length=100, null = True, blank = True)
    contact = models.CharField(max_length=100, null = True, blank = True)
    email = models.EmailField( null = True, blank = True)
    Location = models.CharField(max_length=100, null = True, blank = True)
    TEX =  models.CharField(max_length=100, null = True, blank = True)
    REX = models.CharField(max_length=100, null = True, blank = True)
    Employer = models.CharField(max_length=100, null = True, blank = True)
    PCTC = models.CharField(max_length=100, null = True, blank = True)
    ECTC = models.CharField(max_length=100, null = True, blank = True)
    Notice = models.CharField(max_length=100, null = True, blank = True)
    IntvDate = models.CharField(max_length=100, null = True, blank = True)
    IntvTIme = models.CharField(max_length=100, null = True, blank = True)
    IntvMode = models.CharField(max_length=100, null = True, blank = True)
    Remarks =  models.CharField(max_length=100, null = True, blank = True)
    ConfirmedProjection = models.CharField(max_length=100, null = True, blank = True)
    Doj = models.CharField(max_length=100, null = True, blank = True)
    OfferedCTC = models.CharField(max_length=100, null = True, blank = True)
    VariableCTC =models.CharField(max_length=100, null = True, blank = True)
    BillingPrecentage = models.CharField(max_length=100, null = True, blank = True)
    BillingValue = models.CharField(max_length=100, null = True, blank = True)
    GrossProfit = models.CharField(max_length=100, null = True, blank = True)
    NetProfit = models.CharField(max_length=100, null = True, blank = True)
    RecruterPayout = models.CharField(max_length=100, null = True, blank = True)
                

    def __str__(self):
        return self.name
