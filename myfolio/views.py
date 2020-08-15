from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
import os
import mimetypes
from django.shortcuts import render
from mywebsite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'index.html', {})





