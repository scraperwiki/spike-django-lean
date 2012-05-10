from django.conf.urls.defaults import patterns, include, url
from experiment import pirates_v_zombies, gr
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', pirates_v_zombies, name='home'),
    url(r'^goalrecords/record/([^/])+$', gr, name='goalrecord_record'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
