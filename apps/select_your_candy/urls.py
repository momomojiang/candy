from django.conf.urls import url  
from . import views 

urlpatterns = [
    url(r'^$',views.select),
    url(r'^soft_candy$',views.soft_candy),
    url(r'^hard_candy$',views.hard_candy),
    url(r'^coconut$',views.coconut),
    url(r'^cotton$',views.cotton),
    url(r'^ice_cream$',views.ice_cream),
    url(r'^liquor$',views.liquor),
    url(r'^chocolate$',views.chocolate),
    url(r'^red$',views.red),
    url(r'^orange$',views.orange),
    url(r'^yellow$',views.yellow),
    url(r'^green$',views.green),
    url(r'^indigo$',views.indigo),
    url(r'^blue$',views.blue),
    url(r'^violet$',views.violet),
    url(r'^create_order/(?P<id>\d+)$',views.create_order),
]

