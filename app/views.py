from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.models import Question, Answer, Tag


class ListViewSet:
    class QuestionList(ListView):
        model = Question
        template_name = "app/question/list.html"
        context_object_name = "questions"


class DetailsViewSet:
    class QuestionDetails(DetailView):
        model = Question
        template_name = "app/question/details.html"
        context_object_name = "question"


class CreationViewSet:
    class QuestionCreate(CreateView):
        model = Question
        fields = ['title', 'content', 'tags']
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


def create_answer(request, question_id):
    ans = Answer()
    ans.question = Question.objects.get(pk=question_id)
    ans.author = request.user
    ans.content = request.POST['content']
    ans.is_better = False
    ans.save()
    return HttpResponseRedirect(reverse('question-details', args=(question_id,)))


def related_to(request, tag):
    tag_res = get_object_or_404(Tag, pk=tag)
    res = tag_res.question_set.all()
    return render(request, 'app/question/related.html', {'questions': res, 'tag_name': tag_res})
