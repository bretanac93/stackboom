"""stack_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import ListViewSet, CreationViewSet, UpdateViewSet, DeleteViewSet, DetailsViewSet

urlpatterns = [
    url(r'^$', 'app.views.homepage', name="homepage"),
    url(r'^admin/', admin.site.urls),
    url(r'^questions/$', ListViewSet.QuestionList.as_view(), name='question-list'),
    url(r'^questions/(?P<pk>[0-9]+)/$', DetailsViewSet.QuestionDetails.as_view(), name='question-details'),
    url(r'^questions/create', CreationViewSet.QuestionCreate.as_view(), name='question-create'),
    url(r'^questions/edit/(?P<pk>[0-9]+)/$', UpdateViewSet.QuestionUpdate.as_view(), name='question-edit'),
    url(r'^questions/delete/(?P<pk>[0-9]+)/$', DeleteViewSet.QuestionDelete.as_view(), name='question-delete'),
    url(r'^questions/(?P<question_id>[0-9]+)/answer/$', 'app.views.create_answer', name='make-answer'),
    url(r'^related_to/(?P<tag>[0-9]+)', 'app.views.related_to', name='related-to'),
    url(r'^register/$', 'app.views.register', name="register"),
    url(r'^login/$', 'app.views.login', name='login'),
    url(r'^logout/$', 'app.views.logout', name='logout')
]
