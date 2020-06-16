from django.conf.urls import url
from tickets import views

urlpatterns = [
    url(r'^list/$', views.TicketListView.as_view(), name='list'),
    url(r'^create/$', views.TicketCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', views.TicketUpdateView.as_view(), name='update'),
]
