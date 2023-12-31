from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import MyForm
# Create your views here.

def signupform(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()
    context = {"form": form,}
    formr = loader.get_template('form.html')
    return HttpResponse(formr.render(context, request))