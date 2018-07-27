# howdy/urls.py
from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^tasksList/$', views.TaskListView.as_view()),
    url(r'^apiList/$', views.ApiListView.as_view()),

    url(r'^category/list/$', views.category_list),
    url(r'^category/entity/$', views.category_entity),
    url(r'^category/addEntity/$', views.category_addEntity),
    url(r'^category/moveEntity/$', views.category_moveEntity),
    url(r'^category/deleteEntity/$', views.category_deleteEntity),
]