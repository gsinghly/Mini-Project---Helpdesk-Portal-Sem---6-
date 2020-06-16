from django.conf.urls import url, include
from django.contrib import admin
import helpdesk_portal.views as views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='accounts')),
    url(r'^tickets/', include('tickets.urls', namespace='tickets')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
