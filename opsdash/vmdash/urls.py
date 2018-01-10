from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^digital_ocean', views.digital_ocean_droplets, name='digital_ocean'),
    url(r'^ovh', views.ovh_cloud_projects, name='ovh'),
]
