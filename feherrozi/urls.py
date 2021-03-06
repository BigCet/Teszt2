from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include



from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')),
    path('gallery/', include('gallery.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
