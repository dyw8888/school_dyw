from django.db import models

# Create your models here.


class Patient(models.Model):
    pname = models.CharField(max_length=32, default='姓名')
    pid = models.CharField(max_length=64, null=True)
    pheat = models.FloatField(null=False, default=37.0)
    pgender = models.CharField(max_length=5, default='男', null=False)
    psymptom1 = models.TextField(null=True)
    psymptom2 = models.TextField(null=True)
    psymptom3 = models.TextField(null=True)
    ptime = models.DateTimeField(null=True)

    def __str__(self):
        return self.pname
