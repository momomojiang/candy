from django.conf.urls import url  
from . import views 

urlpatterns = [
    url(r'^(?P<id>\d+)$',views.payment),
    url(r'^make_payment(?P<id>\d+)$',views.make_payment),
    url(r'^successs_purchase(?P<id>\d+)$',views.successs_purchase),
]