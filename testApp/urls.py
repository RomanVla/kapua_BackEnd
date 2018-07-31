# howdy/urls.py
from django.conf.urls import url
from kapua.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view()),

]