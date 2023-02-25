from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Guest


def add_guest(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'guest_add.html')
    guest_data = {
        'user': request.POST.get('user'),
        'email': request.POST.get('email'),
        'text': request.POST.get('text')
    }
    guest = Guest.objects.create(**guest_data)
    return redirect(f'/', context = guest)
