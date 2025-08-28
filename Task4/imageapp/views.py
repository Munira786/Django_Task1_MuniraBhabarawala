from django.shortcuts import render, redirect, get_object_or_404
from .models import ImageModel
from django.core.files.base import ContentFile
from PIL import Image
import io

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        original = request.FILES['image']

        # Save original first
        image_obj = ImageModel.objects.create(original_image=original)

        # Convert to BW
        img = Image.open(image_obj.original_image.path).convert('L')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        image_obj.bw_image.save(
            f"bw_{original.name}",
            ContentFile(buffer.getvalue()),
            save=True
        )

        return render(request, 'success.html', {'image': image_obj})

    return render(request, 'upload.html')


def view_image(request, pk):
    image = get_object_or_404(ImageModel, pk=pk)
    return render(request, 'view_image.html', {'image': image})
