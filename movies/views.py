from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import movie_data
from .forms import movie_form, MovieSearchForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def create(request):
    frm = movie_form()
    if request.POST:
        frm = movie_form(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            return redirect("home")
    else:
        frm = movie_form()

    return render(request, "create.html", {"frm": frm})


def list(request):
    # recently edited movies
    recent_edits = request.session.get("recent_edits", [])
    recent_edits_set = movie_data.objects.filter(pk__in=recent_edits)
    if len(recent_edits) > 3:
        recent_edits.pop()

    # session- view count
    visits = int(request.COOKIES.get("visits", 0))
    visits += 1

    # defining movie_info
    movie_info = movie_data.objects.all()

    # search bar
    search_form = MovieSearchForm(request.GET)
    if search_form.is_valid():
        search = search_form.cleaned_data["query"]
        movie_info = movie_info.filter(title__icontains=search)

    response = render(
        request,
        "list.html",
        {"movies": movie_info, "visits": visits, "recent_edits_set": recent_edits_set},
    )

    # setting cookie
    response.set_cookie("visits", visits)

    return response


@login_required(login_url='login')
def edit(request, pk):
    edit_instance = movie_data.objects.get(pk=pk)
    if request.POST:
        frm = movie_form(request.POST, request.FILES, instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()

            # recent edits  (not consistent)
            recent_edits = request.session.get("recent_edits", [])
            recent_edits.insert(0, pk)
            request.session["recent_edits"] = recent_edits
            return redirect("home")
        else:
            edit_instance = movie_form(instance=edit_instance)
    else:
        frm = movie_form(instance=edit_instance)

    return render(request, "create.html", {"frm": frm})


class ConfirmDeleteView(TemplateView):
    template_name = "confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = kwargs["pk"]
        return context


@login_required(login_url='login')
def delete(request, pk):
    del_instance = movie_data.objects.get(pk=pk)
    if request.method == "POST":
        del_instance.delete()
        return redirect("home")
    return render(
        request, "confirm_delete.html", {"pk": pk, "title": del_instance.title}
    )
