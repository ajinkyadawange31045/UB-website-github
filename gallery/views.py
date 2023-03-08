from django.shortcuts import render,redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import GalleryImage
from .forms import GalleryImageForm


def is_admin(user):
    return user.is_authenticated and user.is_staff

def home(request):
    images = GalleryImage.objects.all()
    # Show most common tags 
    # common_tags = GalleryImage.tags.most_common()[:4]
    context = {
        # 'common_tags': common_tags,
        'images':images
    }

    return render(request,'app/home.html',context)
def details(request, image_id):
    image = get_object_or_404(GalleryImage, pk=image_id)
    previous_image = GalleryImage.objects.filter(pk__lt=image_id).order_by('-pk').first()
    next_image = GalleryImage.objects.filter(pk__gt=image_id).order_by('pk').first()
    context = {
        'image':image,
        'previous_id': previous_image.id if previous_image else None,
        'next_id': next_image.id if next_image else None
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

