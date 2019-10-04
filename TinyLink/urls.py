from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from tiny_link.views import home,link,stats,allLinks
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^allLinks$', allLinks),
    url(r'^(?P<id>\w+)$', link),
    url(r'^(?P<id>\w+)/stats$', stats),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)