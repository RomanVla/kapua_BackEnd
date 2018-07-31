from django.contrib import admin

from django.conf.urls import url
from testApp.views import category_list, category_entity, category_add, category_move, category_delete

urlpatterns = [
	url(r'admin/', admin.site.urls),
    url(r'^category/list/$', category_list),
    url(r'^category/entity/$', category_entity),
    url(r'^category/add/$', category_add),
    url(r'^category/move/$', category_move),
    url(r'^category/delete/$', category_delete),    
]