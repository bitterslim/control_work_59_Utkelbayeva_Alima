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
    return redirect(f'/', pk = guest.pk)


def update_view(request,pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_update.html', context={'guest': guest})
    if request.method == 'POST':
        guest.user = request.POST.get('user')
        guest.email = request.POST.get('email')
        guest.text = request.POST.get('text')
        guest.save()
        return redirect('/', pk=pk)
    return render(request, 'guest_update.html', context={'guest': guest})


def delete_view(request, pk):

    guest = get_object_or_404(Guest, pk=pk)

    if request.method == 'GET':

       return render(request, 'guest_delete.html', context={'guest': guest})

    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
