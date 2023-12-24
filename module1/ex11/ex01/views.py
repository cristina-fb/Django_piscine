from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def djangopage(request):
    template = loader.get_template('base.html')
    nav = loader.get_template('nav.html')
    context = {
        'title': 'Django, framework web',
        'style_file': "style1.css",
        'nav' : nav.render(),
        'text': "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source."
    }
    return HttpResponse(template.render(context, request))

def displaypage(request):
    template = loader.get_template('base.html')
    nav = loader.get_template('nav.html')
    context = {
        'title': 'Display process of a static page',
        'style_file': "style1.css",
        'nav' : nav.render(),
        'text': "To display a web page using Django we have to follow some simple steps. First of all, we need to save our html file in a templates folder inside our app folder. Then, in teh views.py file, we have to load the template and the use the render method so Django can do the rest!"
    }
    return HttpResponse(template.render(context, request))

def templatespage(request):
    template = loader.get_template('base.html')
    nav = loader.get_template('nav.html')
    context = {
        'title': 'Template Engine',
        'style_file': "style2.css",
        'nav' : nav.render(),
        'text': "Sometimes it is really useful to use templates. In the HTML file we use { variable_name } in the place we want to substitute our desirable values. Then in the views.py file, we have to give some context to render the page. In the context dictionary we declare the variables and the values we want for them. You can also use loops to iterate variables. In that case the structure is {% for i in variable_name %}. And that's it!"
    }
    return HttpResponse(template.render(context, request))