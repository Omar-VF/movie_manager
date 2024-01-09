from django.shortcuts import render
from . models import movie_data
from . forms import movie_form
# Create your views here.

def create(request):
    frm=movie_form()
    if request.POST:
        frm=movie_form(request.POST)
        if frm.is_valid:
            frm.save()
        else:
            frm=movie_form()


    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_info=movie_data.objects.all()
    return render(request,'list.html',{'movies':movie_info})

def edit(request,pk):
    return render(request,'edit.html')

def delete(request,pk):
    instance=movie_data.objects.get(pk=pk)
    instance.delete()
    movie_info=movie_data.objects.all()
    return render(request,'list.html',{'movies':movie_info})