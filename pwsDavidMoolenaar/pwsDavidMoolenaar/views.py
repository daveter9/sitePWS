from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(template, request))

def kerkdiensten(request):
    template = loader.get_template('kerkdiensten/index.html')
    return HttpResponse(template.render(template, request))
    
