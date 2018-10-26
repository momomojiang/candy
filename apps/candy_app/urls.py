from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$',views.index, name="main-page"),
    url(r'^create$',views.create, name="create-sweet"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_message'),
]