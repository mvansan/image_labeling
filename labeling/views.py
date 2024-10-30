from django.shortcuts import render, redirect
from .models import Image
from .forms import CaptionForm

def random_image(request):
    if request.method == 'POST':
        image_id = request.session.get('image_id')
        if not image_id:
            return redirect('random_image') 

        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return redirect('random_image')  

        form = CaptionForm(request.POST)
        if form.is_valid():  
            caption = form.cleaned_data.get('caption')

            if not image.caption_1:
                image.caption_1 = caption
            elif not image.caption_2:
                image.caption_2 = caption
            elif not image.caption_3:
                image.caption_3 = caption
            elif not image.caption_4:
                image.caption_4 = caption
            elif not image.caption_5:
                image.caption_5 = caption
            
            image.save()  

            return redirect('random_image')  
        else:
            return render(request, 'random_image.html', {'image': image, 'form': form})

    image = Image.objects.filter(caption_5__isnull=True).order_by('?').first()

    if not image:
        return render(request, 'no_images.html')  

    captions = []
    if image.caption_1:
        captions.append(image.caption_1)
    if image.caption_2:
        captions.append(image.caption_2)
    if image.caption_3:
        captions.append(image.caption_3)
    if image.caption_4:
        captions.append(image.caption_4)
    if image.caption_5:
        captions.append(image.caption_5)

    form = CaptionForm()

    request.session['image_id'] = image.id

    return render(request, 'random_image.html', {'image': image, 'captions': captions, 'form': form})
