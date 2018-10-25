from django.shortcuts import render,redirect, reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Create your views here.
def index(request):
	return render(request, 'candy_app/welcome.html')
# def uploadImg(request):
#     if request.method == "POST":
#         new_img = IMG(
#             img=request.FILES.get('img')
#         )
#         new_img.save()
#     return render(request,'candy_app/uploading.html')

# def showImg(request):
#     imgs = IMG.objects.all()
#     content = {
#         'img':imgs
#     }
#     return render(request, 'candy_app/showing.html', content)

