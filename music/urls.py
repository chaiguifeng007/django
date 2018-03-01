#music/url
from django.urls import path, re_path
from . import views
from .views import UserFormView

app_name = 'music'
urlpatterns = [
    path('', views.as_view(), name='index'),
    re_path(r'^register/$', UserFormView.as_view(), name='register'),
    re_path(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # /music/album/add/
    re_path(r'album/add/$', AlbumCreate.as_view(), name='album-add'),

    re_path(r'album/(?P<pk>[0-9]+)/$', AlbumUpdate.as_view(), name='album-update'),
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', AlbumDelete.as_view(), name='album-delete'),

]