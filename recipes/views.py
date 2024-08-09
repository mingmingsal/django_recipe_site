from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm
from .models import Recipe
from django.views import generic

class IndexView(generic.ListView):
    template_name = "recipes/index.html"
    context_object_name = "recipe_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Recipe.objects.order_by("-pub_date")[:5]



class DetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/details.html"

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            return HttpResponseRedirect("/thanks/")

    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})