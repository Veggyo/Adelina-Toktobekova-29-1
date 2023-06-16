from django.shortcuts import HttpResponse

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date(request):
    if request.method == 'GET':
        return HttpResponse('date: ')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('goodbye user!')
