from django.shortcuts import render
from .forms import ImageForm
from PIL import Image
import torch
import torchvision
from torchvision import transforms
import class_names

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
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            print(type(img_obj.image))
            img = Image.open(img_obj.image)
            print(type(img))

            img_tensor = transform_img(img)

            print(img_tensor.shape)  

            img_tensor = img_tensor.unsqueeze(0)

            print(img_tensor.shape)  

            img_class = torch.argmax( squeezenet(img_tensor) )

            print(img_class)

            img_class_name = class_names.class_name_dict[int(img_class)]

            print(img_class_name)

            img_obj.image_class = img_class_name

            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})
