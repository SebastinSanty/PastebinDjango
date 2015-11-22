from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'pastebinapp.views.home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^([0-9]+)$', 'pastebinapp.views.retrieve'),
    url(r'^admin/', include(admin.site.urls)),
]
