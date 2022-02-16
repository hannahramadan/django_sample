
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('normal', views.normal, name ='normal'),
    path('slow', views.slow, name ='slow'),
    path('rand_error', views.rand_error, name ='rand_error')
]