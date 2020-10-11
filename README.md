# django_pytorch_classifier
Basic django based classifier using pytorch pre-built models

Installation
Python version 3.7.5 other versions of python and packages can work.
1) Create virtual environment
python -m venv .

2) Install django and pytorch  
pip install django==3.1.2  
pip install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html  
Note: CUDA is already enabled in the host machine, if nvcc --version returns the CUDA version use or install CUDA from Nvidia 

3) Clone project to directory  
git clone https://github.com/Hunterhal/django_pytorch_classifier  

4) Create django secret key and change it yours inside the SECRET_KEY  
For this project it is stored in another file, just write your SECRET_KEY there or import from another file  

5) Run and open the server
python manage.py runserver 


TODO:  
Clear saved images inside the media folder, work with temporary files

