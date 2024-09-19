from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def sohaib(request):
    return HttpResponse("Hello sohaib!")

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc")