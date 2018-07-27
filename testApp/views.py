from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Task

class HomePageView(TemplateView):	
    def get(self, request, **kwargs):        
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)

class TaskListView(TemplateView):
    def get(self, request, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})
