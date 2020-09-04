from django.contrib import admin
from . import models
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('pname', 'pid', 'pheat', 'pgender')
    list_filter = ('ptime',)


admin.site.register(models.Patient, PatientAdmin)
