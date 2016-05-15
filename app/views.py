from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Tag

class TagsView:
    class TagsList(ListView):
        model = Tag
        template_name = "app/tag/list.html"

    class TagsDetails(DetailView):
        model = Tag
        template_name = "app/tag/details.html"