'''
Created on 20161028

@author: lch
'''
from django.conf.urls import url,include

urlpatterns = [
    url(r'^news/$', 'app.views.get_news', name='app_news'),
    url(r'^slider/$', 'app.views.get_slider', name='app_slider'),
    url(r'^recom/$', 'app.views.get_recom', name='app_recom'),
]
