from django.shortcuts import render

from django.http import HttpResponse, Http404
import datetime

def hey(request):
    return HttpResponse('<h2>HEY!</h2>')


def current_datetime(request):
    now=datetime.datetime.now()
    context={'now':now}
    return render(request, 'firstApp/now.html', context)


def datetime_plus(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404
    now = datetime.datetime.now()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    context={'dt':dt, 'now':now, 'offset':offset}

    return render(request, 'firstApp/plus.html', context)



