from django.contrib import admin

from django.conf.urls import url
from testApp.views import category_controller

urlpatterns = [
	url(r'admin/', admin.site.urls),

    url(r'^api/list/$', category_controller),
    url(r'^api/move/$', category_controller),
    url(r'^api/delete/$', category_controller),    
    # url(r'^api/entity/$', category_entity),
    # url(r'^api/add/$', category_add),

]