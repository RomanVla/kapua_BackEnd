from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node

class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Api(models.Model):
    httpType = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    params = models.TextField(blank=True, null=True)

    requestExample = models.TextField(blank=True, null=True)
    responseExample = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.httpType +' '+ self.url

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def to_json(self):
        return {'name': self.name}

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'Category: %s' % self.name