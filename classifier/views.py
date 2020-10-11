from django.shortcuts import render
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .forms import ImageForm
from PIL import Image
import torch
import torchvision
from torchvision import transforms
import class_names
import base64





# Create your views here
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        squeezenet = torchvision.models.squeezenet1_0(pretrained=True)

        transform_img = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])

        if form.is_valid():
            #form.save()
            # Get the current instance object to display in the template
            
            img_obj = form.instance

            image = form.cleaned_data['image']
            
            b64_img = base64.b64encode(image.file.read()).decode('utf-8')

            img = Image.open(img_obj.image)

            img_tensor = transform_img(img)

            img_tensor = img_tensor.unsqueeze(0)

            img_class = torch.argmax( squeezenet(img_tensor) )

            img_class_name = class_names.class_name_dict[int(img_class)]

            img_obj.image_class = img_class_name

            return render(request, 'home.html', {'form': form, "img_obj": img_obj, "image": b64_img, "img_class": img_class_name})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})