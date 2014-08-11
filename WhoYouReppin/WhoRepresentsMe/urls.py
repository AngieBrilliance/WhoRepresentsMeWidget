from django.conf.urls import patterns, url
from WhoRepresentsMe import views

urlpatterns = patterns ('',
		url(r'^$', views.index, name='index'),
		url(r'^showLegislators/(?P<address>.+?)$', views.showLegislators, name='showLegislators'),
)