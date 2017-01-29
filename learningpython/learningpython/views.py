from django.shortcuts import render
from learningpython.forms import ContactForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'templates/testtemplate.html', {'current_date': now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form':
form})


