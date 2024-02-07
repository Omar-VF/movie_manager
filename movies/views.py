from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import movie_data
from .forms import movie_form, MovieSearchForm

# Create your views here.


def create(request):
    frm = movie_form()
    if request.POST:
        frm = movie_form(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            return redirect("list")
    else:
        frm = movie_form()

    return render(request, "create.html", {"frm": frm})


def list(request):
    #session- view count
    count = request.session.get('count',0)
    count = int(count)
    count = count+1
    request.session['count']=count

    #defining movie_info
    movie_info = movie_data.objects.all()

    #search bar
    search_form = MovieSearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        movie_info = movie_info.filter(title__icontains=query)
    
    response = render(request, "list.html", {"movies": movie_info,'visits':count})
    return response


def edit(request, pk):
    edit_instance = movie_data.objects.get(pk=pk)
    if request.POST:
        frm = movie_form(request.POST, request.FILES, instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()
            return redirect("list")
        else:
            edit_instance = movie_form(instance=edit_instance)
    else:
        frm = movie_form(instance=edit_instance)

    return render(request, "create.html", {"frm": frm})



class ConfirmDeleteView(TemplateView):
    template_name = 'confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = kwargs['pk']
        return context

def delete(request, pk):
    del_instance = movie_data.objects.get(pk=pk)
    if request.method == 'POST':
        del_instance.delete()
        return redirect('list')
    return render(request, 'confirm_delete.html', {'pk': pk})
