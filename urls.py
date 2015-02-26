from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.defaults import page_not_found

admin.autodiscover()


urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    ("^", include("tema.links.urls")),
    ("^", include("mezzanine.urls")),
    ("comment/", page_not_found),
)

# Adds ``STATIC_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"
