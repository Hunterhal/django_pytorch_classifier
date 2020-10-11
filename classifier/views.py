from django.shortcuts import render
from .forms import ImageForm

# Create your views here
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})
