from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
import datetime
from firstApp.models import Book
from django.core.mail import send_mail

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


#def search_form(request):
   # return render(request, 'firstApp/search_form.html')


def search(request):
    errors=[]

    if 'qq' in request.GET :
        qq=request.GET['qq']

        if qq=='':
            errors.append('Enter a search term.')
        elif len(qq)<3:
            errors.append('Please enter at least 3 characters.')
        else:
            books=Book.objects.filter(title__icontains=qq)

            context={'books':books, 'query':qq}

            return render(request, 'firstApp/search_results.html', context)

    return render(request, 'firstApp/search_form.html', {'errors':errors})



def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, v))
    return HttpResponse('<table>{}</table>'.join(html))

def test_request (request):
    return HttpResponse(request.path)

def mailtest(request):
    subject='subject'
    message='body of message. many mnay many words...'
    from_email='from_maildgango@test.test'
    to_email=['nikitakarpov2013@gmail.com']

    send_mail(subject, message, from_email, to_email)

    return HttpResponse('Message SEND!!!')

def contact(request):
    errors=[]
    if request.method=='POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['nikitakarpov2013@gmail.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'firstApp/contact_form.html',
                  {'errors':errors,
                   'method_get':('GET -',request.GET),
                   'method_post':('POST - ', request.POST),
                   'subject': request.POST.get('subject', ''),
                   'message': request.POST.get('message', ''),
                   'email': request.POST.get('email', '')
                   }
                  )

def contact_thanks(request):
    return HttpResponse('Thanks for message!')



