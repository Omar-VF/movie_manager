from django.shortcuts import render
from . models import movie_data
from . forms import movie_form
# Create your views here.

def create(request):
    frm=movie_form()
    if request.POST:
        frm=movie_form(request.POST,request.FILES)
        if frm.is_valid:
            frm.save()
    else:
        frm=movie_form()


    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_info=movie_data.objects.all()
    return render(request,'list.html',{'movies':movie_info})

def edit(request,pk):
    edit_instance=movie_data.objects.get(pk=pk)
    if request.POST:
        frm=movie_form(request.POST,request.FILES,instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()
    else:
        edit_instance=movie_form(instance=edit_instance)
    frm=movie_form(instance=edit_instance)

        
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    del_instance=movie_data.objects.get(pk=pk)
    del_instance.delete()
    movie_info=movie_data.objects.all()
    return render(request,'list.html',{'movies':movie_info})