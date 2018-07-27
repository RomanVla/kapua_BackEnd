# howdy/urls.py
from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^tasksList/$', views.TaskListView.as_view()),
]