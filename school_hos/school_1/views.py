from django.shortcuts import render
from django.contrib import messages
from . import models
import datetime
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'school_1/login.html')


def log_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    patients = models.Patient.objects.all()
    if (str(username) == 'yiwushi' and str(password) == '123456'):
        return render(request, 'school_1/index.html', {'patients': patients})
    messages.success(request, "用户名或密码错误")


def show_patient(request, patient_id):
    patient = models.Patient.objects.get(pk=patient_id)
    return render(request, 'school_1/show_page.html', {'patient': patient})


def edit_patient(request, patient_id):
    if str(patient_id) == '0':
        time_now = datetime.datetime.now()
        return render(request, 'school_1/edit_patient.html', {'time': time_now})
    patient = models.Patient.objects.get(pk=patient_id)
    return render(request, 'school_1/edit_patient.html', {'patient': patient})


def edit_action(request):
    patient_name = request.POST.get('firstname', '姓名')
    patient_idnumber = request.POST.get('idnumber')
    patient_heat = request.POST.get('heat')
    patient_symptom1 = request.POST.get('symptom_1')
    patient_symptom2 = request.POST.get('symptom_2')
    patient_symptom3 = request.POST.get('symptom_3')
    patient_time = datetime.datetime.now()
    patient_gender_1 = request.POST.get('inlineRadioOptions', '男')
    patient_gender = str(patient_gender_1)
    patient_did = request.POST.get('patient_id')
    if str(patient_did) == '0':
        models.Patient.objects.create(pname=patient_name, pid=patient_idnumber, pheat=patient_heat,
                                      pgender=patient_gender, psymptom1=patient_symptom1, psymptom2=patient_symptom2, psymptom3=patient_symptom3,
                                      ptime=patient_time)
        patients = models.Patient.objects.all()
        return render(request, 'school_1/index.html', {'patients': patients})
    patient = models.Patient.objects.get(pk=patient_did)
    patient.pname = patient_name
    patient.pid = patient_idnumber
    patient.pheat = patient_heat
    patient.pgender = patient_gender
    patient.psymptom1 = patient_symptom1
    patient.psymptom2 = patient_symptom2
    patient.psymptom3 = patient_symptom3
    patient.save()
    return render(request, 'school_1/show_page.html', {'patient': patient})


def search_patient(request):
    nameid_1 = request.POST.get('name_id')
    nameid = str(nameid_1)
    if models.Patient.objects.filter(pid=nameid):
        patients = models.Patient.objects.filter(pid=nameid)
    elif models.Patient.objects.filter(pname=nameid):
        patients = models.Patient.objects.filter(pname=nameid)
    else:
        patients = models.Patient.objects.all()
    return render(request, 'school_1/index.html', {'patients': patients})

    # try:
    #   models.Patient.objects.filter(pid=nameid)
    #  patients = models.Patient.objects.filter(pid=nameid)
    # except models.Patient.DoesNotExist:
    #   try:
    #      models.Patient.objects.filter(pname=nameid)
    #     patients = models.Patient.objects.filter(pname=nameid)
    # except models.Patient.DoesNotExist:
    #   patients = models.Patient.objects.all()
    # return render(request, 'school_1/index.html', {'patients': patients})


def back_index(request):
    patients = models.Patient.objects.all()
    return render(request, 'school_1/index.html', {'patients': patients})
