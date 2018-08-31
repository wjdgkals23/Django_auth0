from django.conf.urls import include,url
from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'^dashboard', views.dashboard),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('social_django.urls', namespace='social')),
]