from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from project_guest.webapp.models import User





def index_view(request: WSGIRequest):
    user = User.objects.all()
    context = {
        'user' : user
    }
    return render(request, 'index.html', context=context)