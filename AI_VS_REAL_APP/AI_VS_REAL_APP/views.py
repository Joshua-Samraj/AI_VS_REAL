from django.shortcuts import render, redirect
from .form import ImageUploadForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')  # simple success page
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
