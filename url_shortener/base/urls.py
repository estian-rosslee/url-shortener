from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:code>', views.detail, name='detail'),
    path('<str:code>/redirect', views.traverse, name='traverse')
]