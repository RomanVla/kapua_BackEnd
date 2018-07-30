from django.conf.urls import url
from testApp.views import TenantView

urlpatterns = [
    url(r'^$', TenantView.as_view()),
]
