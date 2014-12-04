from django.shortcuts import render
from foundation.models import  Page, Headermenu, Portfolio, Title, Develop, Information
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from foundation.forms import ContactForm

def index(request):
    title = Title.objects.all()
    headermenu = Headermenu.objects.all()
    page = Page.objects.all()
    portfolio = Portfolio.objects.all()
    develop = Develop.objects.all()
    information = Information.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    context_dict = {'headermenu':headermenu, 'title':title, 'page':page, 'portfolio':portfolio, 'develop':develop, 'information':information, 'form':form}
    return render (request, 'foundation/index.html', context_dict)



