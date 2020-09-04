from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    url('^login/$', views.login, name='login'),
    url('^logcheck/$', views.log_check, name='logcheck'),
    url('^show/(?P<patient_id>[0-9]+)$',
        views.show_patient, name='show_patient'),
    url('^edit_patient/(?P<patient_id>[0-9]+)$',
        views.edit_patient, name='edit_patient'),
    url('^edit/action$', views.edit_action, name='edit_action'),
    url('^search/$', views.search_patient, name='search_patient'),
    url('^back_index/$', views.back_index, name='back_index')
]


# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
