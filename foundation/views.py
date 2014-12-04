from django.shortcuts import render
from foundation.models import  Page, Headermenu, Portfolio, Title, Develop, Information
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from foundation.forms import ContactForm
from django.core.mail import mail_admins

def index(request):
    title = Title.objects.all()
    headermenu = Headermenu.objects.all()
    page = Page.objects.all()
    portfolio = Portfolio.objects.all()
    develop = Develop.objects.all()
    information = Information.objects.all()
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            # Imaginable form purpose. Post to admins.
            message = """From: %s <%s>\r\nMessage:\r\n%s\r\n""" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            mail_admins('Contact form', message)

            # Only executed with jQuery form request
            if request.is_ajax():
                return HttpResponse('OK')
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here 
                pass
        else:
            if request.is_ajax():
                # Prepare JSON for parsing
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)

                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                # render() form with errors (No AJAX)
                pass
    else:
        form = ContactForm()
    context_dict = {'form':form, 'headermenu':headermenu, 'title':title, 'page':page, 'portfolio':portfolio, 'develop':develop, 'information':information}
    return render (request, 'foundation/index.html', context_dict)

