from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from models import Guest


def index_view(request: WSGIRequest):
    guest = Guest.objects.all()
    context = {
        'guest' : guest
    }
    return render(request, 'index.html', context=context)