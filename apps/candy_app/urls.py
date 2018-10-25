from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$',views.index),
    # url(r'^uploadImg$',views.uploadImg,name="upload_img" ),
    # url(r'^showImg$',views.showImg,name="show_img"),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)