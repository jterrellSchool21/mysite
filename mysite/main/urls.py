from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P[0-9]+)/answer/$', views.answer, name='answer'),
]