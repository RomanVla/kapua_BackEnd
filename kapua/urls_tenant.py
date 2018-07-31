from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from testApp.views import category_list, category_entity, category_addEntity, category_moveEntity, category_deleteEntity

urlpatterns = [
	# path('admin/', admin.site.urls),
	url(r'admin/', admin.site.urls),
    url(r'^category/list/$', category_list),
    url(r'^category/entity/$', category_entity),
    url(r'^category/add/$', category_addEntity),
    url(r'^category/move/$', category_moveEntity),
    url(r'^category/delete/$', category_deleteEntity),    
]