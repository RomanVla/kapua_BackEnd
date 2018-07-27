from django.contrib import admin
from .models import Task, Api, Category

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Task)
admin.site.register(Api)
admin.site.register(Category, MyAdmin)
# Register your models here.
