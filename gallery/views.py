from django.shortcuts import render,redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import GalleryImage
from .forms import GalleryImageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import  HttpResponseRedirect
from django.urls import reverse

def is_admin(user):
    return user.is_authenticated and user.is_staff

from django.shortcuts import render
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import GalleryImage

def home(request):
    images = GalleryImage.objects.all()
    # for image in images:
    #     img = Image.open(image.image)
    #     # Set the maximum size you want here
    #     max_size = (800, 800)
    #     img.thumbnail(max_size, Image.ANTIALIAS)
    #     # Save the image back to memory buffer
    #     in_mem_file = BytesIO()
    #     img.save(in_mem_file, format='JPEG')
    #     # Set the file pointer to the beginning of the buffer
    #     in_mem_file.seek(0)
    #     # Update the image file with the compressed version
    #     image.image = InMemoryUploadedFile(in_mem_file, 'ImageField', "%s.jpg" % image.image.name.split('.')[0], 'image/jpeg', in_mem_file.getvalue(), None)
    #     image.save()

    context = {
        'images':images
    }
    return render(request,'app/home.html',context)


def details(request, image_id):
    image = get_object_or_404(GalleryImage, pk=image_id)
    image.views = image.views + 1
    image.save()
    previous_image = GalleryImage.objects.filter(pk__lt=image_id).order_by('-pk').first()
    next_image = GalleryImage.objects.filter(pk__gt=image_id).order_by('pk').first()
    get_image = GalleryImage.objects.get( id = image_id)
    if request.user in get_image.likes.all() :
        liked = True
    else :
        liked = False
    context = {
        'image':image,
        'previous_id': previous_image.id if previous_image else None,
        'next_id': next_image.id if next_image else None,
        'liked' : liked
    }
    return render(request,'app/details.html',context)


from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def image_upload(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            newImage = form.save(commit=False)
            newImage.save()
            form.save_m2m()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = GalleryImageForm()
        
    return render(request, 'app/image/upload.html', {'form': form})

from django.http import JsonResponse
@login_required
def addlike(request, id) :
    if request.method == "POST" :
        get_img = GalleryImage.objects.get(id = id)
        if request.user not in get_img.likes.all() :
            get_img.likes.add(request.user)
            liked = True
        else :
            get_img.likes.remove(request.user)
            liked = False
        return JsonResponse({'likes_count': len(get_img.likes.all()), 'is_liked': liked})
