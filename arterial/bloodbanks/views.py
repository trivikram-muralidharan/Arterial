from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.http import Http404
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.template import loader
from .models import Donor,Hospital,Bloodbank,BloodReq
import logging
import http.client
import json
from django.http import HttpResponse


def logindonor(request):

    if(request.POST.get("subbtn")):
        usernm = str(request.POST.get('usernm'))
        pswd = str(request.POST.get('pswd'))
        user = authenticate(username=usernm, password=pswd)
        if user is not None:
            login(request, user)

            return redirect('/bloodbanks/indexdonor')

        return redirect('/bloodbanks/indexdonor')


    return render(request,'bloodbanks/logindonor.html')


def loginhospital(request):

    if(request.POST.get("subbtn")):
        usernm = str(request.POST.get('usernm'))
        pswd = str(request.POST.get('pswd'))
        user = authenticate(username=usernm, password=pswd)
        if user is not None:
            login(request, user)

            return redirect('/bloodbanks/indexhospital')

        return redirect('/bloodbanks/indexhospital')


    return render(request,'bloodbanks/loginhospital.html')


def loginbloodbank(request):

    if(request.POST.get("subbtn")):
        usernm = str(request.POST.get('usernm'))
        pswd = str(request.POST.get('pswd'))
        user = authenticate(username=usernm, password=pswd)
        if user is not None:
            login(request, user)

            return redirect('/bloodbanks/indexbloodbank')

        return redirect('/bloodbanks/indexbloodbank')


    return render(request,'bloodbanks/loginbloodbank.html')


def indexhospital(request):

    current_user = request.user
    hospital = Hospital.objects.get(name=current_user.username)
    bbs = Bloodbank.objects.order_by('-name')
    context = {'bbs':bbs}


    if(request.POST.get('update')):
        donor_list = Donor.objects.filter(btype=(request.POST.get('btype')))
        for donor in donor_list:
            donor.bloodreq_set.create(btype=(request.POST.get('btype')),address=hospital.address,hospname=hospital.name,Area=hospital.location,units=(request.POST.get('bunit')))
            return redirect('/bloodbanks/indexhospital')




    

    return render(request,'bloodbanks/indexhospital.html',context)


def indexbloodbank(request):
    current_user = request.user
    bbank = Bloodbank.objects.get(name=current_user.username)
    if(request.POST.get('update')):
        bbank.apunit = (request.POST.get('apunit'))
        bbank.anunit = (request.POST.get('anunit'))
        bbank.bpunit = (request.POST.get('bpunit'))
        bbank.bnunit = (request.POST.get('bnunit'))
        bbank.abpunit = (request.POST.get('abpunit'))
        bbank.abnunit = (request.POST.get('abnunit'))
        bbank.opunit = (request.POST.get('opunit'))
        bbank.onunit = (request.POST.get('onunit'))
        

        bbank.save()

        
        return redirect('/bloodbanks/indexbloodbank/')




    return render(request, 'bloodbanks/indexbloodbank.html',{'bbank':bbank})


    
    return render(request,'bloodbanks/indexbloodbank.html')

def indexdonor(request):
    
    current_user = request.user
    donor = Donor.objects.get(first_name=current_user.username)
    reqs = donor.bloodreq_set.all()
    
    
    return render(request,'bloodbanks/indexdonor.html',context={'reqs':reqs})

