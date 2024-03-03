from django.shortcuts import render, HttpResponse
from json import dumps
from urlredirect.models import URLS
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request, slug):
    object=URLS.objects.filter(slug=slug)
    if object:
        data=dumps({'url':object[0].url})
        return render(request, 'index.html', {'data':data})
    else:
        return render(request, 'error.html')

def addurl(request):
    if request.method=="GET":
        return render(request, 'form.html')
    elif request.method=="POST":
        data=json.loads(request.POST.get('data'))
        db=URLS.objects.filter(slug=data['slug'])
        if db:
            return HttpResponse("Duplicate Slug")
        elif data['slug'] in ['admin', 'post', 'get']:
            return HttpResponse("Provided slug is reserved and cannot be used.")
        else:
            obj=URLS(**data)
            obj.save()
            return HttpResponse("URL Added successfully")
