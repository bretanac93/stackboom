from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.models import Question, Answer


class ListViewSet:
    class QuestionList(ListView):
        model = Question
        template_name = "app/question/list.html"
        context_object_name = "questions"


class CreationViewSet:
    class QuestionCreate(CreateView):
        model = Question
        fields = ['title', 'content', 'author', 'tags']
        template_name = 'app/question/create.html'
        success_url = reverse_lazy('question-list')


class UpdateViewSet:
    class QuestionUpdate(UpdateView):
        model = Question
        fields = ['title', 'content', 'author', 'tags']
        template_name = 'app/question/create.html'
        success_url = reverse_lazy('question-list')


class DeleteViewSet:
    class QuestionDelete(DeleteView):
        model = Question
        success_url = reverse_lazy('question-list')
        template_name = 'app/question/delete.html'
        