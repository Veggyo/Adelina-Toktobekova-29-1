import datetime

from django.shortcuts import HttpResponse

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date(request):
    if request.method == 'GET':
        nowtime = datetime.datetime.now()
        return HttpResponse(f'date:{nowtime} ')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('goodbye user!')
