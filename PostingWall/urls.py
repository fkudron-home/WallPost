from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/post$', views.make_post, name='make_post'),
    url(r'^/register$', views.register, name='register'),
    url(r'^/register_form$', views.register_form, name='register_form'),
]