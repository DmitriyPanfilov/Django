from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('client_orders/', client_orders, name='client_orders'),

]