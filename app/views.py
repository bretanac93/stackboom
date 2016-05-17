from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegistrationForm

from app.models import Question, Answer, Tag


def homepage(request):
    return render(request, 'app/default/index.html')


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


def register(request):
    errors = []
    if request.method == 'POST':
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']

        password = request.POST['password']
        password_confirmation = request.POST['password2']
        if password == password_confirmation:
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            errors.append("The password didn't match")
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request, 'app/auth/register.html', {'errors': errors},
                      context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        access = authenticate(username=username, password=password)
        if access is not None:
            if access.is_active:
                auth.login(request, access)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return render_to_response('app/auth/inactive.html')
        else:
            return render_to_response('app/auth/nouser.html')
    else:
        return render(request, 'app/auth/login.html')

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'app/auth/profile.html', {'user': user})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def about(request):
    return render(request, 'app/default/about.html')


def contact(request):
    return render(request, 'app/default/contact.html')
