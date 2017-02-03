from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.map_prev, name='map_prev'),
]
