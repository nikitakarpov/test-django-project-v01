from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpRequest
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


def search_form(request):
    return render(request, 'firstApp/search_form.html')


def search(request):
    if 'q' in request.GET:
        message='You searched for: {}'.format(request.GET['q'])
    else:
        message = 'You searched an empty form!'
    return HttpResponse(message)

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, v))
    return HttpResponse('<table>{}</table>'.join(html))




