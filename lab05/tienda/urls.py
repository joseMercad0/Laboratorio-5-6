from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index,name='index'),
   # path('producto',views.producto,name='producto'),
]