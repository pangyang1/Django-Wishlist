from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^create$', views.create, name='create'),
    url(r'^item$', views.item, name='item'),
]
