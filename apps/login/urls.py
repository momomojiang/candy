from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="log-reg"),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
	url(r'^logout$', views.logout),
 

]
    # url(r'^edit/(?P<id>\d+)$',views.edit, name="edit_user"),
    # url(r'^update/(?P<id>\d+)$',views.update, name="update_user"),
    
