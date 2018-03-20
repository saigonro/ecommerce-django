
from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_index
from accounts import urls as accounts_urls
from products import urls as products_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'accounts/', include(accounts_urls)),
    url(r'products/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
