from django.shortcuts import render
from django.http import HttpResponse


from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.recipe_name for q in recipe_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)