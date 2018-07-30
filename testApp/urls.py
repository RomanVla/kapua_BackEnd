# howdy/urls.py
from django.conf.urls import url
from kapua.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view()),

    url(r'^category/list/$', views.category_list),
    url(r'^category/entity/$', views.category_entity),
    url(r'^category/addEntity/$', views.category_addEntity),
    url(r'^category/moveEntity/$', views.category_moveEntity),
    url(r'^category/deleteEntity/$', views.category_deleteEntity),
]