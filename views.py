from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse



# Create your views here.


def show(request):
    return render(request,"index.html")


def multipleupload(request):
    return render(request,"index.html")


def savedata(request):
   print(request.FILES)
   if request.method=="post":
       name=request.post.get('name')
       desc=request.post.get('desc')
       image=request.FILES.getlist('file[]')
       Product=Products.objects.create(name=name,desc=desc)
       Product.save()
       PRINT(request.names)
       print(image)

       for img in image:
           fs=FileSystemStorage()
           file_path=fs.save(img.name,img)

           pimage=ProductImages.objects.create(product_id,image=file.path)
           pimage.save()
           
   return redirect("/multi")
