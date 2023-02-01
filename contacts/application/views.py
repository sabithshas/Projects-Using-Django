from django.shortcuts import render,redirect
from .models import contact
# Create your views here.
def index(request):
    data=contact.objects.all()
    return render(request,'index.html',{'data':data})

def add_data(request):
    if request.method =="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        add=contact(name=name,phone=phone,address=address)
        add.save()
        data=contact.objects.all()
        return render (request,'index.html',{'data':data})
    else:
        return render (request,'index.html')

def delete_data(request,item_id):
    item=contact.objects.get(id=item_id)
    item.delete()
    return redirect('home')
        
def edit(request,edit_id):
    data=contact.objects.get(id=edit_id)
    return render(request,'edit.html',{"data":data})

def formupdate(request,update_id):
    if request.method=="POST":
        add=contact.objects.get(id=update_id)
        add.name=request.POST["name"]
        add.phone=request.POST["phone"]
        add.address=request.POST["address"]
        add.save()
        return redirect('home')
