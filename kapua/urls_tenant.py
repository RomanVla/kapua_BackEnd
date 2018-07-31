from django.contrib import admin

from django.conf.urls import url
from testApp.views import category_list, category_entity, category_add, category_move, category_delete

urlpatterns = [
	url(r'admin/', admin.site.urls),
    url(r'^api/category/list/$', category_list),
    url(r'^api/category/entity/$', category_entity),
    url(r'^api/category/add/$', category_add),
    url(r'^api/category/move/$', category_move),
    url(r'^api/category/delete/$', category_delete),    
]