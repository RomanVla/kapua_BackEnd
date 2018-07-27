from django.contrib import admin
from .models import Employees, Task, Product

admin.site.register(Employees)
admin.site.register(Task)
admin.site.register(Product)
# Register your models here.
