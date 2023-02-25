from django.urls import path

from .views.index import index_view
from .views.guest import add_guest

urlpatterns = [
    path('', index_view, name='index'),
    path('guests', index_view, name='index'),
    path('guest/add', add_guest(), name='guest_add')
]
