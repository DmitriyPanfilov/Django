from django.urls import path
from .views import index, client_order

urlpatterns = [
    path('', index, name='index'),
    path('client/<int:client_id>', client_order, name='client_order'),
]