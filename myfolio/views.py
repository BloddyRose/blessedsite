from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        message_email = request.POST.get('email', '')
        try:
            send_mail(message_name, message, message_email, ['bloddy.rose.404@gmail.com'], fail_silently=False)
            return render(request, 'thank.html')
        except:
            return render(request, 'contact.html',
                          {'message_name': message_name, 'message': message, 'from_email': message_email})
    else:
        return render(request, 'contact.html', {})


def thank_page(request):
    return render(request, 'thank.html', {})
