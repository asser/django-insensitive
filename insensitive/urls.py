'''
Created on 2011-06-12

@author: George
'''
try:
    from django.conf.urls import patterns, url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import patterns, url
from insensitive.views import login

urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='auth_login_case_insensitive'),
)

