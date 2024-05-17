
from django.shortcuts import render


from application.forms import ImageForm
from application.models import Image

# Create your views here.
def home(request):
    if request.method=="POST":
       form=ImageForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
    img=Image.objects.all()          
    form=ImageForm()
    return render(request,'home.html',{'img':img,'form':form})