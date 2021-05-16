from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ModeForm
from foodapp.models import sweet


def fun(request):
    items=sweet.objects.all()
    return render(request,'index.html',{'results':items})
def detail(request,id):
    product=sweet.objects.get(id=id)
    return render(request,'detail.html',{'product':product})

def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        s=sweet(name=name,desc=desc,price=price,img=img)
        s.save()
        print("product added")
    return render(request,'add_product.html')




def update(request,id):
    obj=sweet.objects.get(id=id)
    form=ModeForm(request.POST or None ,request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=="POST":
        obj=sweet.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')




