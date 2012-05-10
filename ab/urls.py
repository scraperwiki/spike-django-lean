from django.conf.urls.defaults import patterns, include, url
from experiment import pirates_v_zombies, gr

urlpatterns = patterns('',
    url(r'^$', pirates_v_zombies, name='home'),
    url(r'^goalrecords/record/([^/])+$', gr, name='goalrecord_record'),
)
