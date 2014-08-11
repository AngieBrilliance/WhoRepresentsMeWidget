from django.conf.urls import patterns, url

from WhoRepresentsMe import views

urlpatterns = patterns ('',
		url(r'^$', views.index, name='index'),
)