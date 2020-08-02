from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
import os
import mimetypes


# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        message_email = request.POST.get('email', '')

        send_mail(message_name, message, message_email, ['bloddy.rose.404@gmail.com'], fail_silently=False)
        return render(request, 'thank.html', {})
    else:
        return render(request, 'contact.html', {})


def thank_page(request):
    return render(request, 'thank.html', {})
# Download MTE




